from django.apps import AppConfig
from django.db import connection

class JobsConfig(AppConfig):
    name = 'jobs'

    def ready(self):
        import os
        # Only run if this is the actual server and not a background reloader
        if os.environ.get('RUN_MAIN') == 'true' or os.environ.get('RENDER') == 'true':
            # Check if the table exists before trying to count/seed
            if 'jobs_job' in connection.introspection.table_names():
                try:
                    from .utils import seed_projects
                    seed_projects()
                except Exception as e:
                    print(f"Seeding failed: {e}")