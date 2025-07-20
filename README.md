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

#### Screenshots

![Django Portfolio Site](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/site.jpg "Django Portfolio Site")

###### Django Portfolio Site

![Django Portfolio Admin Page](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/admin_page.jpg "Django Portfolio Admin Page")

###### Django Portfolio Admin Page

![Django Portfolio Updated Details Page](https://raw.githubusercontent.com/joeaoregan/portfolio-django-py/master/screenshots/details_page.jpg "Django Portfolio Details Page")

###### Django Portfolio Updated Details Page. Added embedded YouTube video, and GitHub repo link.

#### References

[Building a Personal Portfolio with Django](https://www.linkedin.com/learning/building-a-personal-portfolio-with-django/)

#### Downloads

[python 3](https://www.python.org/downloads/)  
[django](https://www.djangoproject.com/download/)  
[postgresql](https://www.postgresql.org/download/)  
[pgAdmin 4](https://www.pgadmin.org/download/)
[Bootstrap 4.1 Album example](https://getbootstrap.com/docs/4.1/examples/album/)
[Bootstrap 4.1 Compiled CSS and JS](https://getbootstrap.com/docs/4.1/getting-started/download/)
[jQuery](https://jquery.com/download/)
[Popper](https://unpkg.com/popper.js@1.16.1/dist/umd/popper.min.js)

#### Create Project:

```console
django-admin startproject <project_name>
```

```console
django-admin startapp jobs
```

#### Start App:

```console
python3 manage.py runserver
```

#### Dependencies:

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

#### PostgreSQL

Using pgAdmin 4

```console
\password <username>
```

#### Render

```console
pip install python-dotenv
pip install gunicorn
```

##### Boostrap

Album Example

[Bootstrap 4.1 Album Example](https://getbootstrap.com/docs/4.1/examples/album/)

[Bootstrap 4.1 Quickstart](https://getbootstrap.com/docs/4.1/getting-started/introduction/)

#### Static files

```console
python3 manage.py collectstatic
```
