from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from flask import request
import uuid
from . import db
from .models import User
from . import redisClient
import random


class User_Create(Resource):
    def __init__(self):
        user_create_args= reqparse.RequestParser()
        user_create_args.add_argument("display_name",type=str, help="Display name of the user(STR)", required=False)
        user_create_args.add_argument("country_iso_code",type=str, help="Country iso code of the user(STR)",required=False)
        self.user_create_args=user_create_args
    def post(self):
        args= self.user_create_args.parse_args()
        if args["display_name"]:
            display_name=args["display_name"]
        elif not args["display_name"]:
            display_name= "some_display_name"
        country_code=args["country_iso_code"]

        user_id=str(uuid.uuid4())
        points=0

        user = User(id=user_id, display_name=display_name,country_iso_code=country_iso_code,points=points)

        score_dict={user.id:user.points}
        redisClient.zadd("Leaderboard",score_dict)
        redisClient.zadd(f"Leaderboard/{country_code}",score_dict)
        db.session.add(user)
        db.session.commit()

        pri_rank=redisClient.zrevrank("Leaderboard",user.id)
        rank = pri_rank+1

        response={ 'user_id': user.id, 'display_name':user.display_name, 'country_iso_code': user.country_iso_code, 'points':user.points, 'rank':rank}
        return response,201

class Multiple_User_Create(Resource):
    def post(self):
        req_json=request.json
        if not isinstance(req_json["amount"], int) or req_json["amount"]<1:
            return "Please send a valid amount"
        
        req_data=int(req_json["amount"])

        for i in range(req_data):
            user_id=str(uuid.uuid4())
            country_code="tr"
            display_name="some_display_name"
            random_point=random.randint(1,300)
            points=random_point

            user = User(id=user_id, display_name=display_name,country_iso_code=country_code,points=points)
            score_dict={user.id:user.points}
            redisClient.zadd("Leaderboard",score_dict)
            redisClient.zadd(f"Leaderboard/{country_code}",score_dict)
            db.session.add(user)
            db.session.commit()


        return 201

class User_Profile(Resource):
    def get(self,user_guid):
        user=User.query.filter_by(id=user_guid).first()
        if not user:
            abort(404,message="No such id exists..")

        pri_rank=redisClient.zrevrank("Leaderboard",user_guid)
        rank = pri_rank+1
        response={ 'user_id': user.id, 'display_name':user.display_name, 'points':user.points, 'rank':rank}
        return response,201