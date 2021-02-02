Hello!

!!!This .txt is about the extra endpoints I have created in my REST API and about the cloud service I used, Heroku!!!

You will find comments in each of the python scripts seperately. I also would like to make some clarifications about 
the methods of the scipts, specificaly, how the bonus endpoints work. Every single endpoint you asked for, is created 
in my REST API. I have added a few more endpoints that will ease your testing. 

First (bonus) endpoint is /user/create/multiple. You may want to use this endpoint if you want to create many users at 
once. I want you to send(post) a request of json which should look something like this: {"amount": 1000}. The function
will create that amount(1000 in this case) with display name "some_display_name" and country_name "tr" by default. 
Their user_guid of course will be randomized so they will be unique. These randomly created users will also have random
points between 1,300. This endpoint has a request validation.

!!!IMPORTANT NOTE!!!: There is a timeout in Heroku app. If you try to create, lets say 10,000 users at once, it might
fail to create that many users and return you an error because Heroku has a timeout threshold for each response. If it
exceeds that, it fails.

Second (bonus) endpoint is /score/submit/multiple. You may want to use this endpoint if you want to submit many submissions
at once. I want you to send(post) a request of json type, which should look something like this:
[{"user_guid":"dfbbc141-759b-4d8c-b219-ee50ed3478b9","score_worth":200},
{"user_guid":"2e2a0acc-9cb0-4b7e-b6ab-d3881f34738d","score_worth":200},
....].
The function will parse the json elements, and update the user scores individually in a for loop. Their user_guids 
of course should be specified along with score_worth. 


"ABOUT HEROKU"
I have deployed my code in my Git-Hub repo to heroku server with Redis. It is currently working on there quite good. 
You can send post/get requests and get corresponding responses. 
You can send your requests to f"https://gjg-restapi.herokuapp.com/{endpoint}". For example to create multiple users,
send request to https://gjg-restapi.herokuapp.com/user/create/multiple with a proper request body.
I ll keep the server running for you. However if it remains inactive for sometime, it changes its status to down. That 
means it erases its database and its Redis sorted list.


"ALL ENDPOINTS AND THEIR PROPER REQUESTS"
I write here the proper request bodies required for each endpoint in case you ll be lost. I created the patterns
considering the sample runs you sent in your document.

ENDPOINT : "/leaderboard/<string:country_code>", REQUEST TYPE: GET,  REQUEST BODY: NONE(EMPTY)
ENDPOINT : "/leaderboard", REQUEST TYPE: GET,  REQUEST BODY: NONE(EMPTY)
ENDPOINT : "/score/submit", REQUEST TYPE: POST,  REQUEST BODY: {"user_guid":user_guid, "score_worth":score_worth}
ENDPOINT : "/score/submit/multiple", REQUEST TYPE: POST,  REQUEST BODY: [{"user_guid":user_guid, "score_worth":score_worth},
									{"user_guid":user_guid, "score_worth":score_worth},
									.....]

#display_name and country_iso_code is not required here. If not given, display name will be "some_display_name"
#country_iso_code will be "tr"
ENDPOINT : "/user/create", REQUEST TYPE: POST,  REQUEST BODY: {"display_name":display_name, "country_iso_code":country_iso_code}

#Please indicate how many users you want to create at once(like 1000 in the example). 
# Just a heads up for you. It took me approximately 10ish seconds to create 1000 users in Heroku.
ENDPOINT : "/user/create/multiple", REQUEST TYPE: POST,  REQUEST BODY: {"amount":1000}

ENDPOINT : "/user/profile/<string:user_guid>", REQUEST TYPE: GET, REQUEST BODY: NONE(empty)


It was an amazing experience to work on such a project. I really do hope to hear from you again.
