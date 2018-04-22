from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
moon = Flask(__name__)

# Configurations
moon.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(moon)

# Register blueprint(s)
from app.blueprints.www.controllers import mod_www # to avoid import problems we will import the modules just before registration
moon.register_blueprint(mod_www)

# Sample HTTP error handling
@moon.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404
	
# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all()
