import os
import connexion

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


## Here's where all the info for start the app is.
## It will be called by start.py & build_database.py


# instead of hardcode to ./ we get the abs address from the one of this file
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion - Flask wrapper instance and loads the path for the swagger file
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy as a part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# LINUX WAY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')
# WINDOWS WAY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////people.db'
# not event driven app.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
