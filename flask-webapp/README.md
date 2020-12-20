#install sudo apt update
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
sudo apt 
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools


#

#https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04
install redis on ubuntu 20.04

source venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt



#App Context
#https://www.xspdf.com/resolution/50572705.html

https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/

https://dev.to/kaelscion/authentication-hashing-in-sqlalchemy-1bem

#https://hackersandslackers.com/flask-application-factory
#http://allynh.com/blog/reusing-flask-sql-alchemy-code-between-multiple-applications/
#http://allynh.com/blog/adding-an-api-to-your-flask-project/
#https://testdriven.io/blog/flask-contexts-advanced/


#SQLAlchemy models in and out of app context
#https://stackoverflow.com/questions/21243291/flask-sqlalchemy-when-are-the-tables-databases-created-and-destroyed
#https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables
#https://stackoverflow.com/questions/41004540/using-sqlalchemy-models-in-and-out-of-flask/41014157
#https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4


#SQLAlchemy checks create_all
#https://stackoverflow.com/questions/40652938/flask-sqlalchemy-check-if-table-exists-in-database
#https://overiq.com/flask-101/database-modelling-in-flask/
#https://stackoverflow.com/questions/21243291/flask-sqlalchemy-when-are-the-tables-databases-created-and-destroyed

#Flask SQLAlchemy video and code
#https://www.youtube.com/watch?v=XTpLbBJTOM4
#https://codeloop.org/flask-crud-application-with-sqlalchemy/


########################################
#Required routes
#http://localhost:7000/
- landing page, welcomes anonymous user with options to goto Home, ToDo after login
- show login and Sign-up links
- if user clicks on login, show user email and password
- on successful login show Home
- if user clicks Sign-up show signup form
- on successful sign-up, redirect to login
 

#http://localhost:7000/todo/
- show logged in user's todo list


#######################
#db model to tables creation with migrate
#https://qxf2.com/blog/database-migration-flask-migrate/
#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
