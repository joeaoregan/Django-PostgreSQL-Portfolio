from django.apps import AppConfig
from django.db import connection
from django.db.utils import OperationalError

class JobsConfig(AppConfig):
    name = 'jobs'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import os
        # Only attempt to seed if we are running the actual server
        if os.environ.get('RUN_MAIN') == 'true' or os.environ.get('RENDER') == 'true':
            try:
                # Check if the table exists
                if 'jobs_job' in connection.introspection.table_names():
                    from .utils import seed_projects
                    seed_projects()
            except (OperationalError, Exception) as e:
                # If DB is down, print to logs but DON'T crash the app
                print(f"Database seeding skipped: {e}")