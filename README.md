
Website Status Checker with AWS Lambda and SNS
Overview:
This Lambda function checks the status of websites and sends an Amazon SNS alert if any website is down. Below are the step-by-step instructions to set up the solution.


Here's the README.md file content structured as bullet points for easy reference:






in the  lambda_function.py file 
1 check  arn first 
 files  will  directon like 


 website_status_checker/
├── lambda_function.py
└── python/

it means a main folder then all files will therere 

##################################################
#####################################################
################################################
Check all website statsu and if down  send sns service 


##################################################
#####################################################
################################################



step: 1 

   Set Up Amazon SNS:
   Click on Topics in the left sidebar.
   Click on Create topic.
   Choose Standard as the type.
   Enter a name for your topic (e.g., WebsiteStatusAlerts).
   Click Create topic.   

step: 2

    Subscribe to the Topic:
    After creating the topic, click on it to open the topic details.
    Click on Create subscription.
    For the Protocol, select Email.
    For the Endpoint, enter your email address where you want to receive notifications.
    Click Create subscription.
    Check your email for a subscription confirmation and follow the link to confirm the subscription.


step: 3

    Create a New Function:
    Click on Create function.
    Choose Author from scratch.
    Enter a name for your function (e.g., WebsiteStatusChecker).
    Set the Runtime to Python 3.x.
    For Permissions, choose Create a new role with basic Lambda permissions.
    Click on Create function.
    after createion lamda funtion
        open specific function
         go to configurtion > Permission >  see the  name "Role name" under role name you will see a new role name click on it 
         and it will  land you to IAM user  you need to and a  new role 
     when open role of this lamda  go to permisson >add permission> create inline policy and pase the code 


//////////////////////////////
////////////////////////////
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "*"
    }
  ]
}
////////////////////////////
///////////////////////////
put this to  IAM role inline policy



Step : 4 :

   Crete folder :

   create a new folder  to you local machine 
   cerate  lambda_function.py and requirement.txt 
   past the code and requrentmt files into it 
   for this only need request  
   pip install requests -t .
   or 
   pip install --no-user -r requirements.txt -t . //for windows

   after install packages  cretea a zip files for this 
   then  go back to lamada that is craeted some time erliar 
   then upload this zip file 
   then create a test   file 
    and test the code if got any erro copy and past chatgpt or other to solve tthis 
    after successfully run the code you will see a message and  check added emains 


step : 5

    Create schedule to run this python code  every 30m after : 

step 6 :
 
    setup  triger/ schedule 
    create  trigger from lamda function
    create a role 
    set crontab /timer  ex: rate(30 minutes) 
    then select terget  

    check  this  script ,,


    finish




