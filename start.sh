python3 models.py && PGPASSWORD=password psql -h postgres -U postgres -d postgres -f create_views.sql && python3 spacex_loader.py && python3 generate_fake_data.py