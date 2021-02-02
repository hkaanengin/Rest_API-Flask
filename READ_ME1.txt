Hello!

!!!This .txt is about the extra endpoints I have created in my REST API!!!

You will find comments in each of the python scripts seperately. I also would like to make some clarifications about 
the methods of how the scipts, specificaly, how the bonus endpoints work. Every single endpoint you asked for, is created 
in my REST API. I have added a few more endpoints that will ease your testing. 

First (bonus) endpoint is /user/create/multiple. You may want to use this endpoint if you want to create many users at 
once. I want you to send(post) a request of json which should look something like this: {"amount": 1000}. The function
will create that amount(1000 in this case) with display name "some_display_name" and country_name "tr" by default. 
Their user_guid of course will be randomized so they will be unique. These randomly created users will also have random
points between 1,300. This endpoint has a request validation.

Second (bonus) endpoint is /score/submit/multiple. You may want to use this endpoint if you want to submit many submissions
at once. I want you to send(post) a request of json, which should look something like this:
[{"user_guid":"dfbbc141-759b-4d8c-b219-ee50ed3478b9","score_worth":200},
{"user_guid":"2e2a0acc-9cb0-4b7e-b6ab-d3881f34738d","score_worth":200}].
The function will parse the json elements, and update the user scores individually in a for loop. Their user_guids 
of course should be specified along with score_worth. 

It was an amazing experience to work on such a project. I really do hope to hear from you again.