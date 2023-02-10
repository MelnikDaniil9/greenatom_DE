query_rockets = """
{
  rockets {
    active
    boosters
    company
    cost_per_launch
    country
    description
    diameter {
      feet
      meters
    }
    engines {
      engine_loss_max
      layout
      number
      propellant_1
      propellant_2
      thrust_sea_level {
        kN
        lbf
      }
      thrust_to_weight
      thrust_vacuum {
        kN
        lbf
      }
      type
      version
    }
    first_flight
    first_stage {
      burn_time_sec
      engines
      fuel_amount_tons
      reusable
    }
    height {
      feet
      meters
    }
    id
    landing_legs {
      material
      number
    }
    mass {
      kg
      lb
    }
    name
    payload_weights {
      id
      kg
      lb
      name
    }
    second_stage {
      burn_time_sec
      engines
      fuel_amount_tons
      payloads {
        composite_fairing {
          diameter {
            feet
            meters
          }
          height {
            feet
            meters
          }
        }
        option_1
      }
      thrust {
        kN
        lbf
      }
    }
    stages
    success_rate_pct
    type
    wikipedia
  }
}
"""

query_missions = """
{
  missions {
    description
    id
    manufacturers
    name
    payloads {
      customers
      id
      manufacturer
      nationality
      norad_id
      orbit
      orbit_params {
        apoapsis_km
        arg_of_pericenter
        eccentricity
        epoch
        inclination_deg
        lifespan_years
        longitude
        mean_anomaly
        mean_motion
        periapsis_km
        period_min
        raan
        reference_system
        regime
        semi_major_axis_km
      }
      payload_mass_kg
      payload_mass_lbs
      payload_type
      reused
    }
    twitter
    website
    wikipedia
  }
}
"""

query_launches = """
{
  launches {
    details
    id
    is_tentative
    launch_date_local
    launch_date_unix
    launch_date_utc
    launch_site {
      site_id
      site_name
      site_name_long
    }
    launch_success
    launch_year
    links {
      article_link
      flickr_images
      mission_patch
      mission_patch_small
      presskit
      reddit_campaign
      reddit_launch
      reddit_media
      reddit_recovery
      video_link
      wikipedia
    }
    mission_id
    mission_name
    rocket {
      fairings {
        recovered
        recovery_attempt
        reused
        ship
      }
      first_stage {
        cores {
          block
          core {
            asds_attempts
            asds_landings
            block
            id
            missions {
              flight
              name
            }
            original_launch
            reuse_count
            rtls_attempts
            rtls_landings
            status
            water_landing
          }
          flight
          gridfins
          land_success
          landing_intent
          landing_type
          landing_vehicle
          legs
          reused
        }
      }
      rocket {
        active
        boosters
        company
        cost_per_launch
        country
        description
        diameter {
          feet
          meters
        }
        engines {
          engine_loss_max
          layout
          number
          propellant_1
          propellant_2
          thrust_sea_level {
            kN
            lbf
          }
          thrust_to_weight
          thrust_vacuum {
            kN
            lbf
          }
          type
          version
        }
        first_flight
        first_stage {
          burn_time_sec
          engines
          fuel_amount_tons
          reusable
        }
        height {
          feet
          meters
        }
        id
        landing_legs {
          material
          number
        }
        mass {
          kg
          lb
        }
        name
        payload_weights {
          id
          kg
          lb
          name
        }
        second_stage {
          burn_time_sec
          engines
          fuel_amount_tons
          payloads {
            composite_fairing {
              diameter {
                feet
                meters
              }
              height {
                feet
                meters
              }
            }
            option_1
          }
          thrust {
            kN
            lbf
          }
        }
        stages
        success_rate_pct
        type
        wikipedia
      }
      rocket_name
      rocket_type
      second_stage {
        block
        payloads {
          customers
          id
          manufacturer
          nationality
          norad_id
          orbit
          orbit_params {
            apoapsis_km
            arg_of_pericenter
            eccentricity
            epoch
            inclination_deg
            lifespan_years
            longitude
            mean_anomaly
            mean_motion
            periapsis_km
            period_min
            raan
            reference_system
            regime
            semi_major_axis_km
          }
          payload_mass_kg
          payload_mass_lbs
          payload_type
          reused
        }
      }
    }
    ships {
      abs
      active
      attempted_landings
      class
      course_deg
      home_port
      id
      image
      imo
      missions {
        flight
        name
      }
      mmsi
      model
      name
      position {
        latitude
        longitude
      }
      roles
      speed_kn
      status
      successful_landings
      type
      url
      weight_kg
      weight_lbs
      year_built
    }
    static_fire_date_unix
    static_fire_date_utc
    telemetry {
      flight_club
    }
    tentative_max_precision
    upcoming
  }
}
"""
