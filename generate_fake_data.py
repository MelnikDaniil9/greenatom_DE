import datetime
import random
from time import sleep

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import (CONNECTION, Launch, LaunchLinks, LaunchRocket, LaunchSite,
                    Mission, Payload, PayloadOrbitParams, Rocket,
                    RocketEngines, RocketFirstStage, RocketLandingLegs,
                    RocketSecondStage)

N = 15

if __name__ == "__main__":
    engine = create_engine(CONNECTION)

    with Session(engine) as session:
        fake = Faker()

        while True:
            sleep(30)
            for i in range(N):
                orbit_params = PayloadOrbitParams(
                    apoapsis_km=random.uniform(400, 600),
                    arg_of_pericenter=random.uniform(0, 360),
                    eccentricity=random.uniform(0, 1),
                    epoch=datetime.datetime.now(),
                    inclination_deg=random.uniform(0, 180),
                    lifespan_years=random.uniform(5, 10),
                    longitude=random.uniform(0, 360),
                    mean_anomaly=random.uniform(0, 360),
                    mean_motion=random.uniform(1, 2),
                    periapsis_km=random.uniform(400, 600),
                    period_min=random.uniform(500, 1000),
                    raan=random.uniform(0, 360),
                    reference_system=fake.text(),
                    regime=fake.text(),
                    semi_major_axis_km=random.uniform(400, 600),
                )
                session.add(orbit_params)

                mission = Mission(
                    description=fake.text(),
                    id=fake.uuid4(),
                    manufacturers=[fake.company() for j in range(random.randint(1, 5))],
                    name=fake.company_suffix(),
                    twitter=fake.user_name(),
                    website=fake.url(),
                    wikipedia=fake.url(),
                )
                session.add(mission)

                payload = Payload(
                    customers=[fake.company() for j in range(random.randint(1, 5))],
                    id=fake.uuid4(),
                    manufacturer=fake.company(),
                    nationality=fake.country_code(),
                    norad_id=[random.randint(1, 10000) for j in range(random.randint(1, 5))],
                    orbit=fake.word(),
                    payload_mass_kg=random.uniform(0, 10000),
                    payload_mass_lbs=random.uniform(0, 10000),
                    payload_type=fake.word(),
                    reused=random.choice([True, False]),
                )
                payload.mission = mission
                payload.orbitparams = orbit_params
                session.add(payload)

            for i in range(N):
                rocket_engine = RocketEngines(
                    engine_loss_max=fake.text(),
                    layout=fake.text(),
                    number=random.randint(1, 10000),
                    propellant_1=fake.word(),
                    propellant_2=fake.word(),
                    thrust_sea_level_kN=random.uniform(0, 10000),
                    thrust_sea_level_lbf=random.uniform(0, 10000),
                    thrust_to_weight=random.uniform(0, 10000),
                    thrust_vacuum_kN=random.uniform(0, 10000),
                    thrust_vacuum_lbf=random.uniform(0, 10000),
                    type=fake.word(),
                    version=fake.word(),
                )
                session.add(rocket_engine)

                first_stage = RocketFirstStage(
                    burn_time_sec=random.randint(1, 10000),
                    engines=random.randint(1, 10000),
                    fuel_amount_tons=random.uniform(0, 10000),
                    reusable=random.choice([True, False]),
                    thrust_sea_level_kN=random.uniform(0, 10000),
                    thrust_sea_level_lbf=random.uniform(0, 10000),
                    thrust_vacuum_kN=random.uniform(0, 10000),
                    thrust_vacuum_lbf=random.uniform(0, 10000),
                )
                session.add(first_stage)

                second_stage = RocketSecondStage(
                    burn_time_sec=random.randint(1, 10000),
                    engines=random.randint(1, 10000),
                    fuel_amount_tons=random.uniform(0, 10000),
                    option_1=fake.word(),
                    diameter_feet=random.uniform(0, 10000),
                    diameter_meters=random.uniform(0, 10000),
                    height_meters=random.uniform(0, 10000),
                    kN=random.uniform(0, 10000),
                    lbf=random.uniform(0, 10000),
                )
                session.add(second_stage)

                landing_legs = RocketLandingLegs(
                    material=fake.word(),
                    number=random.randint(1, 10000),
                )
                session.add(landing_legs)

                rocket = Rocket(
                    id=fake.uuid4(),
                    active=random.choice([True, False]),
                    boosters=random.randint(0, 10000),
                    company=fake.company(),
                    cost_per_launch=random.randint(0, 10000),
                    country=fake.country(),
                    description=fake.text(),
                    diameter_feet=random.uniform(0, 10000),
                    diameter_meters=random.uniform(0, 10000),
                    first_flight=datetime.datetime.now(),
                    height_feet=random.uniform(0, 10000),
                    height_meters=random.uniform(0, 10000),
                    mass_kg=random.randint(0, 10000),
                    mass_lb=random.randint(0, 10000),
                    name=fake.word(),
                    stages=random.randint(0, 10000),
                    success_rate_pct=random.randint(0, 10000),
                    type=fake.word(),
                    wikipedia=fake.url(),
                )
                rocket.engine = rocket_engine
                rocket.first_stage = first_stage
                rocket.second_stage = second_stage
                rocket.landing_leg = landing_legs
                session.add(rocket)

            for i in range(N):
                launchlinks = LaunchLinks(
                    article_link=fake.url(),
                    flickr_images=[fake.word() for j in range(random.randint(1, 5))],
                    mission_patch=fake.word(),
                    mission_patch_small=fake.word(),
                    presskit=fake.word(),
                    reddit_campaign=fake.url(),
                    reddit_launch=fake.url(),
                    reddit_media=fake.url(),
                    reddit_recovery=fake.url(),
                    video_link=fake.url(),
                    wikipedia=fake.url(),
                )
                session.add(launchlinks)

                launchsite = LaunchSite(site_id=fake.uuid4(), site_name=fake.word(), site_name_long=fake.word())
                session.add(launchsite)

                launchrocket = LaunchRocket(
                    fairings=[fake.word() for j in range(random.randint(1, 5))],
                    first_stage=[fake.word() for j in range(random.randint(1, 5))],
                    rocket=[fake.word() for j in range(random.randint(1, 5))],
                    rocket_name=fake.word(),
                    rocket_type=fake.word(),
                    second_stage=[fake.word() for j in range(random.randint(1, 5))],
                )
                session.add(launchrocket)

                launch = Launch(
                    id=fake.uuid4(),
                    details=fake.text(),
                    is_tentative=random.choice([True, False]),
                    launch_date_local=datetime.datetime.now(),
                    launch_date_unix=random.randint(1675000000, 1679000000),
                    launch_date_utc=datetime.datetime.now(),
                    launch_success=random.choice([True, False]),
                    launch_year=fake.word(),
                    mission_name=fake.word(),
                    ships=[fake.word() for j in range(random.randint(1, 5))],
                    static_fire_date_unix=random.randint(1675000000, 1679000000),
                    static_fire_date_utc=datetime.datetime.now(),
                    flight_club=fake.word(),
                    tentative_max_precision=fake.word(),
                    upcoming=random.choice([True, False]),
                    mission_id=[random.randint(1, 10000) for j in range(random.randint(1, 5))],
                )
                launch.launchsite = launchsite
                launch.launchlinks = launchlinks
                launch.launchrocket = launchrocket
                session.add(launch)

            session.commit()
