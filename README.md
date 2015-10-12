
#searchinstructor
Search unimag instructor

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/local/bin/python3
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the git repository

```bash
git init
git remote add origin git@github.com:/searchinstructor.git
```

Migrate, create a superuser, and run the server:

```bash
python search_instructor/manage.py migrate
python search_instructor/manage.py createsuperuser
python search_instructor/manage.py runserver
```

