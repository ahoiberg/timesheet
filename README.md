Basic timesheet written using Flask to track hours worked by a single user

Created to track how long I work on side projects

Currently using an SQLite DB, will probably migrate that if/when this gets deployed

To initialize database, run:

'''
flask initdb
'''

To run the applicaiton locally:

'''
flask run
'''



Plan for MVP:

1/23: create database, be able to create entry for each instance of hours logged (also confirm this approach is correct)

1/24: be able to collate weekly totals

1/26: add some styling 