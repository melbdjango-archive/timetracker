# MelbDjango School - Time Tracker

## What's all this then?

This simple time tracker application is our first of many demo applications
for future [MelbDjango School](http://melbdjangoschool.com/) lessons and
classes.

It's also a place for us to experiment with things that we might want to
discuss during the lessons. You might see things in here that we won't touch
on during the classes (see: @sesh's quick property lesson), and this won't
encompass everything that's tought.


## Installation

It's highly recommended that you use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
if it's compatible with your operating system.

To get started developing, all you should need to do is:

    mkvirtualenv melbdjango-timetracker
    git clone https://github.com/MelbDjango/timetracker.git
    pip install -Ur requirements.txt

Once the requirements are installed, you can migrate your database and
create your first (super)user:

    chmod +x manage.py
    ./manage.py migrate
    ./manage.py createsuperuser

At the moment the application is completely driven by the Django admin.
Over the next few weeks we'll be adding more views and perhaps a simple
REST API as a way to teach about APIs, views and templates.

To run the application simply run server and open `http://localhost:8000/admin/`
in your browser.

    ./manage.py runserver
