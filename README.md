# Task_interview_shopify

## To run this project 

To run this project you will be needing a docker and docker-compose installed in your system.
You just need to run "docker-compose up" to start the api api will be running on 8087 port. of your localhost.

## Requests
HTTP POST: 
/add
Request: 
Response: 
Status: 200 OK 
{
“messsage": ”Product added successfully”
}

HTTP GET: 
/retrive 

Response: Data retrived from database. 

HTTP PUT: 
/update 
Request: 

Response: 
Status: 200 OK 
{"message":
                        True}

HTTP DELETE: 
/remove 
Request: 
{
    "id": "61d90636f551cbaeb8ec7c30"
}

Response: 
Status: 200 OK 
true

