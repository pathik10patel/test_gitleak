# Task_interview_shopify

## To run this project 

To run this project you will be needing a docker and docker-compose installed in your system.
You just need to run "docker-compose up" to start the api api will be running on 8087 port. of your localhost.
To Download the csv file open the html file and click on the download button file will be downloaded in the docker.

![download-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/export_data.PNG)
![csv-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/export_data_response.PNG)

## Requests
HTTP POST: 
/add
Request: 
![add-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/add.PNG)
Response: 
Status: 200 OK 
{
“messsage": ”Product added successfully”
}

HTTP GET: 
/retrive 
Request: 
![retrive-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/retrive.PNG)
Response: Data retrived from database. 

HTTP PUT: 
/update 
Request: 
![update-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/update.PNG)
Response: 
Status: 200 OK 
{"message":True}

HTTP DELETE: 
/remove 
Request: 
![remove-request](https://github.com/pathik10patel/Task_interview_shopify/blob/main/screenshots/remove.PNG)
Response: 
Status: 200 OK 
true

