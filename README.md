# Trading System
For Technical Test

## Pre-requisites
- Code Editor
- Python 3
- Web Browser

## Start Guide
1. Install git: https://git-scm.com/downloads.
2. Set up your git with your github account.
2. Install pipenv in the command line: `pip3 install pipenv`
  - Make sure folder to Python3 is configured in your PATH.
2. Go to directory or folder to put project.
3. Run these commands in bash or command line:

```
cd <directory>

python -m venv env
cd env
cmd: Scripts\activate
bash: source ./Scripts/activate
pip install django
pip install djangorestframework
pip install django-simple-history

cd <directory>

git clone https://github.com/jonahmarc/tradingsystem.git
cd tradingsystem
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Go to the address specified (http://127.0.0.1:8000/) to see development site.

```
python manage.py createsuperuser
```
7. Go to (http://127.0.0.1:8000/admin) to see the admin dashboard and use the newly created superuser credentials.