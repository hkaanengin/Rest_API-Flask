# LEADERBOARD REST API

## Table of Contents
- [Introduction](#introduction)
- [Endpoints](#endpoints)
- [Request Examples](#request-examples)
- [Heroku Server](#heroku-server)

## Introduction

The aim of this project is to create a real-time leaderboard for a game. The created endpoints consists the actions of creating players, submitting scores,
displaying the leaderboard and much more.. 

Once the players are created, they gain points by submitting scores. As soon as the leaderboard has a new input, either a new player created or a new score submission made,
it immediately ranks its players by their scores, acting as a real-time sorting leaderboard.

Each player has a unique identifier(uuid), username(display_name), country(country iso code) and score. You can create one/multiple players(s), have a look at 
player' profiles, update one/multiple player(s)' score and display the leaderboard either globally or country specificly by using the endpoints which are explained in detail below.

For this project, I used FLASK to deal with the API part and Heroku as a cloud service to host my API.

## Endpoints

Following endpoints are exposed to be used:

- **/leaderboard**: (GET) Return global leaderboard
- **/leaderboard/{country_iso_code}**: (GET) Returns country specific leaderboard
- **/user/create**: (POST) Creates a player with specified player name and country iso code
- **/user/create/multiple**: (POST) Creates a specified amount of player with the name `display_name` and country iso code `tr`
- **/score/submit**: (POST) Submit the specified amount of score for a player
- **/score/submit/multiple**: (POST) Submit scores for multiple players
- **/user/profile/<string:user_guid>**: (GET) Returns profile of a player.

## Request Examples

| Endpoint      | Request Type | Request Body Example |
| ----------- | ----------- | --- |
| **/leaderboard** | GET   | NONE(EMPTY REQUEST)|
| **/leaderboard/{country_iso_code}**   | GET | NONE(EMPTY REQUEST) |
| **/score/create** | POST | {"display_name":display_name, "country_iso_code":country_iso_code}|
| **/score/create/multiple**| POST        | {"amount":1000} |
| **/user/submit** | POST  | {"user_guid":user_guid, "score_worth":score_worth}|
| **/user/submit/multiple** | POST  | [{"user_guid":user_guid, "score_worth":score_worth},{"user_guid":user_guid, "score_worth":score_worth}, ...] |
| **/user/profile/{user_guid}** | GET  | NONE(EMPTY REQUEST) |

## Heroku Server
The whole script has been deployed on a Heroku server(Free Tier) with Redis. It should still be currently working. However you might have to send a couple of requests to wake the server up. While doing that, please do expect some bad response. The reason is that the server remains inactive for a while, it changes its status to idle, deletes the database and goes to sleep. 

You can send your requests to: 
```bash
https://gjg-restapi.herokuapp.com**<endpoint>
```

For example:
```bash
https://gjg-restapi.herokuapp.com/leaderboard
```