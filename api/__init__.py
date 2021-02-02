from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from flask import request
import uuid
import redis
import rq
import random
from os import path
import os

db = SQLAlchemy()
DB_NAME="database.db"
redisClient = redis.StrictRedis(host="redis-19766.c226.eu-west-1-3.ec2.cloud.redislabs.com",port=19766,db=0, password="OPouC22LHDZcuQfGCtAIctWZC3DI5fye")


#redisClient = redis.StrictRedis(host="127.0.0.1",port=6379,db=0)
def create_app():

    app= Flask(__name__)
    api= Api(app)
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    

    from .models import User
    from .user_scores import Score_Submit, Multiple_Score_Submit
    from .user_profiles import User_Create, Multiple_User_Create, User_Profile
    from .leaderboards import Leaderboard, Leaderboard_Country

    
    create_database(app)

    api.add_resource(Leaderboard_Country,"/leaderboard/<string:country_code>")
    api.add_resource(Leaderboard, "/leaderboard")
    api.add_resource(Score_Submit, "/score/submit")
    api.add_resource(Multiple_Score_Submit, "/score/submit/multiple")
    api.add_resource(User_Create, "/user/create") #Post
    api.add_resource(Multiple_User_Create, "/user/create/multiple")
    api.add_resource(User_Profile, "/user/profile/<string:user_guid>")  #Get

    return app

def create_database(app):
    if not path.exists('api/'+DB_NAME):
        print(os.environ.get("DATABASE_URL"))
        redisClient.flushall()
        db.create_all(app=app)
        print('Created Database!')