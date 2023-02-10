import sqlalchemy
from sqlalchemy import (Boolean, Column, Date, Float, ForeignKey, Integer,
                        String, create_engine)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


CONNECTION = "postgresql://postgres:password@postgres:5432/postgres"


class RocketEngines(Base):
    __tablename__ = "RocketEngines"
    id = Column(Integer, primary_key=True, autoincrement=True)
    engine_loss_max = Column(String(512))
    layout = Column(String(512))
    number = Column(Integer)
    propellant_1 = Column(String(512))
    propellant_2 = Column(String(512))
    thrust_sea_level_kN = Column(Float)
    thrust_sea_level_lbf = Column(Float)
    thrust_to_weight = Column(Float)
    thrust_vacuum_kN = Column(Float)
    thrust_vacuum_lbf = Column(Float)
    type = Column(String(512))
    version = Column(String(512))

    rocket = relationship("Rocket", back_populates="engine")


class RocketLandingLegs(Base):
    __tablename__ = "RocketLandingLegs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    material = Column(String(512))
    number = Column(Integer)

    rocket = relationship("Rocket", back_populates="landing_leg")


class RocketFirstStage(Base):
    __tablename__ = "RocketFirstStage"
    id = Column(Integer, primary_key=True, autoincrement=True)
    burn_time_sec = Column(Integer)
    engines = Column(Integer)
    fuel_amount_tons = Column(Float)
    reusable = Column(Boolean)
    thrust_sea_level_kN = Column(Float)
    thrust_sea_level_lbf = Column(Float)
    thrust_vacuum_kN = Column(Float)
    thrust_vacuum_lbf = Column(Float)

    rocket = relationship("Rocket", back_populates="first_stage")


class RocketSecondStage(Base):
    __tablename__ = "RocketSecondStage"
    id = Column(Integer, primary_key=True, autoincrement=True)
    burn_time_sec = Column(Integer)
    engines = Column(Integer)
    fuel_amount_tons = Column(Float)
    option_1 = Column(String(512))
    diameter_feet = Column(Float)
    diameter_meters = Column(Float)
    height_feet = Column(Float)
    height_meters = Column(Float)
    kN = Column(Float)
    lbf = Column(Float)

    rocket = relationship("Rocket", back_populates="second_stage")


class Rocket(Base):
    __tablename__ = "Rocket"
    id = Column(String(36), primary_key=True)
    active = Column(Boolean)
    boosters = Column(Integer)
    company = Column(String(512))
    cost_per_launch = Column(Integer)
    country = Column(String(512))
    description = Column(String(512))
    diameter_feet = Column(Float)
    diameter_meters = Column(Float)
    first_flight = Column(Date)
    height_feet = Column(Float)
    height_meters = Column(Float)
    mass_kg = Column(Integer)
    mass_lb = Column(Integer)
    name = Column(String(512))
    stages = Column(Integer)
    success_rate_pct = Column(Integer)
    type = Column(String(512))
    wikipedia = Column(String)

    engines_id = Column(Integer, ForeignKey("RocketEngines.id"), unique=True)
    first_stage_id = Column(Integer, ForeignKey("RocketFirstStage.id"), unique=True)
    landing_legs_id = Column(Integer, ForeignKey("RocketLandingLegs.id"), unique=True)
    second_stage_id = Column(Integer, ForeignKey("RocketSecondStage.id"), unique=True)

    engine = relationship("RocketEngines", back_populates="rocket")
    first_stage = relationship("RocketFirstStage", back_populates="rocket")
    landing_leg = relationship("RocketLandingLegs", back_populates="rocket")
    second_stage = relationship("RocketSecondStage", back_populates="rocket")
    payload_weights = relationship("RocketPayloadWeight", back_populates="rocket")


class RocketPayloadWeight(Base):
    __tablename__ = "RocketPayloadWeight"
    surrogate_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(32))
    kg = Column(Integer)
    lb = Column(Integer)
    name = Column(String(512))
    rocket_id = Column(String(36), ForeignKey("Rocket.id"))

    rocket = relationship("Rocket", back_populates="payload_weights")


class LaunchLinks(Base):
    __tablename__ = "LaunchLinks"
    links_id = Column(Integer, primary_key=True, autoincrement=True)
    article_link = Column(String(512))
    flickr_images = Column(JSONB)
    mission_patch = Column(String(512))
    mission_patch_small = Column(String(512))
    presskit = Column(String(512))
    reddit_campaign = Column(String(512))
    reddit_launch = Column(String(512))
    reddit_media = Column(String(512))
    reddit_recovery = Column(String(512))
    video_link = Column(String(512))
    wikipedia = Column(String(512))

    launch = relationship("Launch", back_populates="launchlinks")


class LaunchSite(Base):
    __tablename__ = "LaunchSite"
    site_id = Column(String(36), primary_key=True)
    site_name = Column(String(512))
    site_name_long = Column(String(512))

    launch = relationship("Launch", back_populates="launchsite")


class LaunchRocket(Base):
    __tablename__ = "LaunchRocket"
    rocket_id = Column(Integer, primary_key=True, autoincrement=True)
    fairings = Column(JSONB)
    first_stage = Column(JSONB)
    rocket = Column(JSONB)
    rocket_name = Column(String(512))
    rocket_type = Column(String(512))
    second_stage = Column(JSONB)

    launch = relationship("Launch", back_populates="launchrocket")


class Launch(Base):
    __tablename__ = "Launch"
    id = Column(String(36), primary_key=True)
    details = Column(String(2048))
    is_tentative = Column(Boolean)
    launch_date_local = Column(Date)
    launch_date_unix = Column(Integer)
    launch_date_utc = Column(Date)
    launch_success = Column(Boolean)
    launch_year = Column(String(512))
    mission_name = Column(String(2048))
    ships = Column(JSONB)
    static_fire_date_unix = Column(Integer)
    static_fire_date_utc = Column(Date)
    flight_club = Column(String(2048))
    tentative_max_precision = Column(String(2048))
    upcoming = Column(Boolean)
    mission_id = Column(JSONB)

    launch_site_id = Column(String(36), ForeignKey("LaunchSite.site_id"), unique=True)
    links_id = Column(Integer, ForeignKey("LaunchLinks.links_id"), unique=True)
    rocket_id = Column(Integer, ForeignKey("LaunchRocket.rocket_id"), unique=True)

    launchsite = relationship("LaunchSite", back_populates="launch")
    launchlinks = relationship("LaunchLinks", back_populates="launch")
    launchrocket = relationship("LaunchRocket", back_populates="launch")


class Mission(Base):
    __tablename__ = "Mission"
    description = Column(String(512))
    id = Column(String(36), primary_key=True)
    manufacturers = Column(JSONB)
    name = Column(String(512))
    twitter = Column(String(512))
    website = Column(String(512))
    wikipedia = Column(String(512))

    payload = relationship("Payload", back_populates="mission")


class Payload(Base):
    __tablename__ = "Payload"
    customers = Column(JSONB)
    id = Column(String(36), primary_key=True)
    manufacturer = Column(String(512))
    nationality = Column(String(512))
    norad_id = Column(JSONB)
    orbit = Column(String(512))
    payload_mass_kg = Column(Float)
    payload_mass_lbs = Column(Float)
    payload_type = Column(String(512))
    reused = Column(Boolean)

    orbit_params_id = Column(Integer, ForeignKey("PayloadOrbitParams.id"), unique=True)
    mission_id = Column(String(36), ForeignKey("Mission.id"), unique=True)

    orbitparams = relationship("PayloadOrbitParams", back_populates="payload")
    mission = relationship("Mission", back_populates="payload")


class PayloadOrbitParams(Base):
    __tablename__ = "PayloadOrbitParams"
    id = Column(Integer, primary_key=True, autoincrement=True)
    apoapsis_km = Column(Float)
    arg_of_pericenter = Column(Float)
    eccentricity = Column(Float)
    epoch = Column(Date)
    inclination_deg = Column(Float)
    lifespan_years = Column(Float)
    longitude = Column(Float)
    mean_anomaly = Column(Float)
    mean_motion = Column(Float)
    periapsis_km = Column(Float)
    period_min = Column(Float)
    raan = Column(Float)
    reference_system = Column(String(512))
    regime = Column(String(512))
    semi_major_axis_km = Column(Float)

    payload = relationship("Payload", back_populates="orbitparams")


if __name__ == "__main__":
    engine = create_engine(CONNECTION)
    Base.metadata.create_all(engine)
