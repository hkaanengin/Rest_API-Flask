from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from flask import request
import uuid
from . import db


class User(db.Model):
    __tablename__='users'
    #id = db.Column(db., primary_key=True)
    id = db.Column(db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    #user_id = db.Column(db.String(50), nullable=False)
    display_name = db.Column(db.String(50), nullable=True)
    country_iso_code= db.Column(db.String, nullable=True)
    points = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"User(id={id}, display_name={display_name}, country_iso_code={country_iso_code}, points={points}"

