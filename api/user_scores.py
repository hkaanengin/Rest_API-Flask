from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from flask import request
import uuid
from . import db
from .models import User
from datetime import datetime
from . import redisClient


class Score_Submit(Resource):
    def __init__(self):
        point_upgrade_args = reqparse.RequestParser()
        point_upgrade_args.add_argument("user_guid",type=str, help="User ID of the user(STR)", required=True)
        point_upgrade_args.add_argument("score_worth",type=int, help="Score worth", required=True)

        self.point_upgrade_args=point_upgrade_args
    def post(self):

        args=self.point_upgrade_args.parse_args()
        user_guid=args["user_guid"]
        score_worth=args["score_worth"]
        now = datetime.now()
        timestamp=datetime.timestamp(now)


        result=User.query.filter_by(id=user_guid).first()
        if not result:
            abort(404, message="User ID doesnt exists, cannot update")
        if args['score_worth']:
            result.points = result.points + args['score_worth']
        country_code=result.country_iso_code
        score_dict={user_guid:result.points}

        redisClient.zadd("Leaderboard",score_dict)
        redisClient.zadd(f"Leaderboard/{country_code}",score_dict)
        db.session.commit()

        response={'score_worth':score_worth, 'user_id': user_guid,'timestamp': timestamp}
        return response,201

class Multiple_Score_Submit(Resource): 
    def post(self):
        req_json=request.json
        resp_json=[]
        for req in req_json:
            user_guid=req["user_guid"]
            score_worth=req["score_worth"]
            now = datetime.now()
            timestamp=datetime.timestamp(now)
            result=User.query.filter_by(id=user_guid).first()
            if not result:
                abort(404, message="User ID doesnt exists, can not update")
            if req["score_worth"]:
                result.points = result.points + score_worth

            country_code=result.country_iso_code
            score_dict={user_guid:result.points}
            redisClient.zadd("Leaderboard",score_dict)
            redisClient.zadd(f"Leaderboard/{country_code}",score_dict)
            db.session.commit()
            resp_each={'score_worth':score_worth, 'user_id': user_guid,'timestamp': timestamp}

            resp_json.append(resp_each)

        return resp_json,201
