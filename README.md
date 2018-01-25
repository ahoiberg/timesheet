Basic timesheet written using Flask to track hours worked by a single user

Created to track how long I work on side projects

Currently using an SQLite DB, will probably migrate that if/when this gets deployed

This is best run with virtualenv, install ```sudo pip install virtualenv```

To set up your virtual environment, run:

```
virtualenv -p python3 env
```

To activate, run:

```
source env/bin/activate
```

Install your python dependencies
```
pip install -r requirements.txt
```

To initialize database, run:

```
flask initdb
```

Note that this will destory any existing information, so be careful

To run the application locally:

```
flask run
```

