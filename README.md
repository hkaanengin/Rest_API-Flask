# REST API WITH FLASK
Hello, 
This main aim of this project is to create a REST API endpoint that manages a game that uses a leaderboard with players submitting new scores from around the world. The service will only be responsible for submitting
player scores and returning leaderboard data either globally or country-specific. Players gain points by submitting scores and they are placed on the leaderboard by their scores. The player with the highest score will be at the top I am going to give you detailed information about the endpoints that I have created in my REST API and the cloud server I used, Heroku.

You will find comments in each of the python scripts seperately. I also would like to make some clarifications about the methods of the scripts, specificaly, how the bonus endpoints work. These bonus endpoints is to work in big numbers. 

Endpoints:
* The endpoint is exposed at **/leaderboard** (GET)
* By default it will return global leaderboard (no specific country)
* For country specific queries, it is exposed at **/leaderboard/{country_iso_code}** (GET)
* Score submission endpoint is exposed at **/score/submit** (POST)
* User profile endpoint is exposed at **/user/profile/{user_guid}** (GET)
* User create endpint is exposed at **/user/create** (POST)
* All IDs should be GUIDs
* Each score submission can affect the ranking of any players below them.
* All endpoints will accept JSON and/or return JSON responses

Bonus Endpoints:
* Multiple user create endpoint is exposed at **/user/create/multiple**
* Multiple user submission endpoint is exposed at **/score/submit/multiple**


##Proper Requests for Each Endpoints

| Endpoint      | Request Type | Request Body Example |
| ----------- | ----------- | --- |
| **/leaderboard** | GET   | NONE(EMPTY REQUEST)|
| **/leaderboard/{country_iso_code}**   | GET | NONE(EMPTY REQUEST) |
| **/score/create** | POST | {"display_name":display_name, "country_iso_code":country_iso_code}|
| **/score/create/multiple**| POST        | {"amount":1000} |
| **/user/submit** | POST  | {"user_guid":user_guid, "score_worth":score_worth}|
| **/user/submit/multiple** | POST  | [{"user_guid":user_guid, "score_worth":score_worth},{"user_guid":user_guid, "score_worth":score_worth}, ...] |
| **/user/profile/{user_guid}** | GET  | NONE(EMPTY REQUEST) |

The table above shows the request types, request body examples(if there should be one) for each endpoint exists in the REST API.
Request Body example for multiple user create endpoint contains "amount" value in it. That indicates the number of users to be created in the database. Every users will be assigned an unique user_guid with country iso code "tr" and a random score points.

You can send your requests to **https://gjg-restapi.herokuapp.com**+(Endpoint). 
For example; **https://gjg-restapi.herokuapp.com/leaderboard**

## Deployement on Heroku
The whole script has been deployed on a Heroku server(Free Tier) with Redis. It is still currently working. However you might have to send a couple of requests to wake the server up. Meanwhile, please do expect some bad response. The reason is that the server remains inactive for a while, it changes its status to idle, deletes the database and goes to sleep. 