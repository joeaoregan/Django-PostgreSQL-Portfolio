# Python/Django Portfolio Tutorial

## Joe O'Regan

[See App On Render](https://django-postgresql-portfolio.onrender.com/)

Tutorial from LinkedIn Learning [here](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

- Django
- PostgreSQL
- Bootstrap (jQuery, Popper)

Added extra fields to database for project name and GitHub repo link

---

[![YouTube Django PostgreSQL Portfolio](https://img.youtube.com/vi/9lGoAAfoc3k/default.jpg)](https://youtu.be/9lGoAAfoc3k)
[![YouTube Django PostgreSQL Portfolio Update](https://img.youtube.com/vi/MN3ClQzpw_k/default.jpg)](https://youtu.be/MN3ClQzpw_k)

###### YouTube Links

---

#### Start App:

```console
python3 manage.py runserver
```

<details>
  <summary>1. Screenshots</summary>

![Django Portfolio Site](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/site.jpg "Django Portfolio Site")

###### Django Portfolio Site

![Django Portfolio Admin Page](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/admin_page.jpg "Django Portfolio Admin Page")

###### Django Portfolio Admin Page

![Django Portfolio Updated Details Page](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/details_page.jpg "Django Portfolio Details Page")

###### Django Portfolio Updated Details Page. Added embedded YouTube video, and GitHub repo link.

</details>

<details>
  <summary>2. References</summary>

[Building a Personal Portfolio with Django](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

</details>

<details>
  <summary>3. Downloads</summary>

[python 3](https://www.python.org/downloads/)  
[django](https://www.djangoproject.com/download/)  
[postgresql](https://www.postgresql.org/download/)  
[pgAdmin 4](https://www.pgadmin.org/download/)
[Bootstrap 4.1 Album example](https://getbootstrap.com/docs/4.1/examples/album/)
[Bootstrap 4.1 Compiled CSS and JS](https://getbootstrap.com/docs/4.1/getting-started/download/)
[jQuery](https://jquery.com/download/)
[Popper](https://unpkg.com/popper.js@1.16.1/dist/umd/popper.min.js)

</details>

<details>
  <summary>4. Dependencies</summary>

```console
pip3 install pillow
```

Communicate with PostgreSQL database:

```console
pip3 install psycopg2
```

```console
pip3 install psycopg2-binary
```

</details>

<details>
  <summary>5. Create Project</summary>

```console
django-admin startproject <project_name>
```

```console
django-admin startapp jobs
```


###### Note to Self: Run the next 2 commands after updating database fields

```console
python3 manage.py makemigrations
```

```console
python3 manage.py migrate
```

```console
python3 manage.py createsuperuser
```

</details>

<details>
  <summary>5. PostgreSQL</summary>

Using pgAdmin 4

```console
\password <username>
```

</details>

<details>
  <summary>6. Render</summary>

```console
pip install python-dotenv
pip install gunicorn
```

</details>

<details>
  <summary>7. Boostrap</summary>

Album Example

[Bootstrap 4.1 Album Example](https://getbootstrap.com/docs/4.1/examples/album/)

[Bootstrap 4.1 Quickstart](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

</details>

<details>
  <summary>8. Static files</summary>

```console
python3 manage.py collectstatic
```

</details>



<details>
  <summary>9. Sample Data</summary>

## Admin Page

Local: `http://localhost:8000/admin/` \
Render: `https://django-postgresql-portfolio.onrender.com/admin/`


### Project #1: Zombie Apocalypse

Name: `Zombie Apocalypse` \
Image: `1_zombie.jpg` \
Summary: `Zombie Apocalypse Unity Game created for semester 7 module Platform Digital Game Engines.` \
Link: `https://github.com/joeaoregan/LIT-Yr4-DigitalGameEngines` \
YouTube: `https://youtu.be/V1eb564VPUw`

### Project #2: Antibody

Name: `Antibody` \
Image: `2_antibody.jpg` \
Summary: `Antibody, a 2D side scrolling game created with C++ and SDL2 for my third year Group Project.` \
Link: `https://github.com/joeaoregan/LIT-Yr3-Project-Antibody` \
YouTube: `https://youtu.be/f0VTU8N0e6I`

### Project #3: JOR_Net

Name: `JOR_Net` \
Image: `3_yr4.jpg` \
Summary: `JOR_Net, my 4th year project, a library for creating networked games in C/C++ using SDL2.` \
Link: `https://github.com/joeaoregan/LIT-Yr4-Project-NetworkGamesLibrary` \
YouTube: `https://youtu.be/88U7cKIl8VU`
  
</details>