from .models import Job

def seed_projects():
    if Job.objects.count() == 0:
        # Add your default projects here
        Job.objects.create(
            name="Zombie Apocalypse",
            summary="Zombie Apocalypse Unity Game created for semester 7 module Platform Digital Game Engines.",
            link="https://github.com/joeaoregan/LIT-Yr4-DigitalGameEngines",
            image="images/1_zombie.jpg",
            youtube="ruvsSkgFk3s"
        )
        Job.objects.create(
            name="Antibody",
            summary="Antibody, a 2D side scrolling game created with C++ and SDL2 for my third year Group Project.",
            link="https://github.com/joeaoregan/LIT-Yr3-Project-Antibody",
            image="images/2_antibody.jpg",
            youtube="f0VTU8N0e6I"
        )
        Job.objects.create(
            name="JOR_Net",
            summary="JOR_Net, my 4th year project, a library for creating networked games in C/C++ using SDL2.",
            link="https://github.com/joeaoregan/LIT-Yr4-Project-NetworkGamesLibrary",
            image="images/3_yr4.jpg",
            youtube="88U7cKIl8VU"
        )

        print("Database seeded with default projects!")

from django.contrib.auth.models import User
import os

def seed_superuser():
    username = os.environ.get("ADMIN_USERNAME", "admin")
    email = os.environ.get("ADMIN_EMAIL", "admin@example.com")
    password = os.environ.get("ADMIN_PASSWORD")

    if password and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully!")        
