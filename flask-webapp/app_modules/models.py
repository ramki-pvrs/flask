"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from sqlalchemy.sql import func

from . import db


class User(UserMixin, db.Model):
    """Model for user accounts."""
    #Set the name of the resulting table.
    __tablename__ = "users"

    #Sets the Postgres schema to save the table under.
    __table_args__ = {"schema":"todo_app"}

    #Specifies that a table with this name already exists in the target database. When this is set, your model will not override existing tables Thus, it is possible that the fields in your model might not match up with columns in your table.
    __table_args__ = {"extend_existing":True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    website = db.Column(db.String(255), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.name)

class ToDo(db.Model):
    """Model for todo list by user."""
    #Set the name of the resulting table.
    __tablename__ = "todo"

    #Sets the Postgres schema to save the table under.
    __table_args__ = {"schema":"todo_app"}

    #Specifies that a table with this name already exists in the target database. When this is set, your model will not override existing tables Thus, it is possible that the fields in your model might not match up with columns in your table.
    __table_args__ = {"extend_existing":True}

    id = db.Column(db.Integer, primary_key=True)
    ownerid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task = db.Column(db.Text, nullable=False) 
    comment = db.Column(db.Text, nullable=False) 
    status = db.Column(db.Enum('Open', 'Completed', 'On-Hold', 'Invalid', name='statuses'), nullable=False)
    createrid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, server_default=func.now())
    updated = db.Column(db.DateTime, onupdate=func.now())
 
