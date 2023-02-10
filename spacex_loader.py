import requests
from sqlalchemy.orm import Session

from models import *
from spacex_graphql_queries import query_launches, query_rockets

url = "https://spacex-production.up.railway.app/"

if __name__ == "__main__":
    engine = create_engine(CONNECTION)

    with Session(engine) as session:
        rockets = requests.post(url, json={"query": query_rockets}).json()["data"]["rockets"]
        for rocket in rockets:
            engines = rocket.pop("engines", {})
            first_stage = rocket.pop("first_stage", {})
            landing_legs = rocket.pop("landing_legs", {})
            payload_weights = rocket.pop("payload_weights", [])
            second_stage = rocket.pop("second_stage", {})

            # create Rocket
            diam = rocket.pop("diameter", {})
            diameter = {
                "diameter_feet": diam.get("feet"),
                "diameter_meters": diam.get("meters"),
            }
            h = rocket.pop("height", {})
            height = {
                "height_feet": h.get("feet"),
                "height_meters": h.get("meters"),
            }
            m = rocket.pop("mass", {})
            mass = {
                "mass_kg": m.get("kg"),
                "mass_lb": m.get("lb"),
            }
            rocket_ = Rocket(**rocket, **diameter, **height, **mass)

            # create RocketEngines
            tsl = engines.pop("thrust_sea_level", {})
            trust_sea_level = {
                "thrust_sea_level_kN": tsl.get("kN"),
                "thrust_sea_level_lbf": tsl.get("lbf"),
            }
            tv = engines.pop("thrust_vacuum", {})
            trust_vacuum = {
                "thrust_vacuum_kN": tsl.get("kN"),
                "thrust_vacuum_lbf": tsl.get("lbf"),
            }
            engines = RocketEngines(**engines, **trust_sea_level, **trust_vacuum)
            rocket_.engine = engines

            # create FirstStage
            first_stage = RocketFirstStage(**first_stage)
            rocket_.first_stage = first_stage

            # create LandingLegs
            landing_legs = RocketLandingLegs(**landing_legs)
            rocket_.landing_leg = landing_legs

            # create PayloadWeight
            payload_weights = [RocketPayloadWeight(**pw) for pw in payload_weights]
            rocket_.payload_weights = payload_weights

            # create SecondStage
            payloads = second_stage.pop("payloads", {})
            composite_fairing = payloads.get("composite_fairing")
            diam = composite_fairing.pop("diameter", {})
            diameter = {
                "diameter_feet": diam.get("feet"),
                "diameter_meters": diam.get("meters"),
            }
            h = composite_fairing.pop("height", {})
            height = {
                "height_feet": h.get("feet"),
                "height_meters": h.get("meters"),
            }
            payloads = {**diameter, **height, "option_1": payloads.get("option_1")}
            thrust = second_stage.pop("thrust", {})
            second_stage = RocketSecondStage(**second_stage, **payloads, **thrust)
            rocket_.second_stage = second_stage
            session.add(rocket_)

        launches = requests.post(url, json={"query": query_launches}).json()["data"]["launches"]

        for launch in launches:
            launch_site = launch.pop("launch_site", {})
            links = launch.pop("links", {})
            rocket = launch.pop("rocket", {})

            # create Launch
            telemetry = launch.pop("telemetry", {})
            if telemetry:
                flight_club = telemetry.get("flight_club")
            else:
                flight_club = None
            launch_ = Launch(**launch, flight_club=flight_club)

            # create LaunchSite
            if launch_site:
                launch_site = LaunchSite(**launch_site)
                launch_.launchsite = launch_site

            # create LaunchLinks
            if links:
                links = LaunchLinks(**links)
                launch_.launchlinks = links

            # create LaunchRocket
            if rocket:
                rocket = LaunchRocket(**rocket)
                launch_.launchrocket = rocket

            session.add(launch_)

        session.commit()  # insert all data
