from flask_restful import Resource
from . import db, redisClient
from .models import User

'''Since you have not specified how many people should "/Leaderboard" endpoint return, I thought 20 would be a good number. If you want to increase the amount,
    please do change the "0,19" parameters to your liking in each Leaderboard class(Leaderboar&Leaderboard_Country).'''
    
class Leaderboard(Resource):
    def get(self):

        sorted_list=redisClient.zrevrange("Leaderboard",0,19)
        leaderboard_list=[]
        for ele_concat in sorted_list:
            user_guid=str(ele_concat).split("'")[1]
            result=User.query.filter_by(id=user_guid).first()
            if not result:
                continue
            display_name=result.display_name
            country_name=result.country_iso_code
            user_total_points=result.points
            pri_rank=redisClient.zrevrank("Leaderboard",user_guid)
            rank = pri_rank+1
            user_profile={"rank": rank,"points": user_total_points,"display_name": display_name, "country": country_name}
            leaderboard_list.append(user_profile)
        return leaderboard_list,201


class Leaderboard_Country(Resource):
    def get(self, country_code):

        sorted_list=redisClient.zrevrange(f"Leaderboard/{country_code}",0,19)
        country_leaderboard_list=[]

        for ele_concat in sorted_list:
            user_guid=str(ele_concat).split("'")[1]
            result=User.query.filter_by(id=user_guid).first()
            display_name=result.display_name
            country_name=result.country_iso_code
            user_total_points=result.points
            pri_rank=redisClient.zrevrank("Leaderboard",user_guid)
            rank = pri_rank+1       
            user_profile={"rank": rank,"points": user_total_points,"display_name": display_name, "country": country_name}
            country_leaderboard_list.append(user_profile)

        return country_leaderboard_list,201