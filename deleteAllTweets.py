# so you want to delete all your tweets...

# a developer account is required, in order to get your api key. don't 
# worry, the free version is enough, with this method. 

# here is a ai summary of how to get a developer account:

"""1. Sign Up or Log In to X

Begin by visiting X’s Developer Platform. If you don’t already have an X account, 
you’ll need to create one. This account will be linked to your developer credentials.

2. Apply for Developer Access
Once logged in, navigate to the developer portal and click on “Apply” or “Create an App.” 
You’ll be prompted to provide information about how you intend to use X’s APIs. You can be honest.


3. Complete the Application Form
Fill out the application form with accurate and detailed information. You may be asked about:

4. Wait for Approval
After submitting your application, X will review your request. This process can take anywhere 
from a few hours to several days, depending on the volume of applications and the details you provided.

5. Access Your Developer Dashboard
Once approved, you’ll receive an email notification. You can then access your developer dashboard, 
where you can create and manage your apps, generate API keys, and monitor usage.

6. Create an App and Generate Keys
Within the dashboard, create a new app. This will provide you with the necessary API keys and tokens 
to authenticate your requests to X’s API."""

# this method requires requesting your archive. heres a ai summary of how to do that:

"""Log in to Twitter:

Go to twitter.com and log in to your account.
Access Account Settings:

Click on your profile picture in the top-right corner and select Settings and privacy.
Navigate to "Your Account":

In the left-hand menu, click on Your account.
Request Your Archive:

Under Download an archive of your data, click Request archive.
Twitter will send a notification or email once your archive is ready for download.

This step takes around 24 hrs.

Download the Archive:

Follow the link provided in the notification or email to download your archive as a .zip file.
Extract the Archive:

Unzip the file to access your data, including tweets, media, and account information."""

# fill out the file location of the 'tweets.js' file. find file, under a couple of folder layers
# (its in a data folder) press get info, copy the location

file_location = " "

# Replace these with your own API credentials
API_KEY = " "
API_SECRET = " "
ACCESS_TOKEN = " "
ACCESS_TOKEN_SECRET = " "


# Read the tweets.js file, strip JS assignment, and save as JSON  
with open(file_location + 'tweets.js', 'r', encoding='utf-8') as f:  
    content = f.read()  
  
# Find the first '[' and last ']' to extract the JSON array  
start = content.find('[')  
end = content.rfind(']') + 1  
json_content = content[start:end]  
  
file_location = " "
with open(file_location+ "tweets.json", "r") as f:
    tweets = json.load(f)


# Save to tweets.json  
with open('tweets.json', 'w', encoding='utf-8') as f:  
    f.write(json_content)  
import tweepy
from datetime import datetime
import json
from datetime import datetime






# Initialize the API client
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)



# Verify authentication
try:
    user = api.verify_credentials()
    print(f"Authenticated as: {user.screen_name}")
except Exception as e:
    print(f"Authentication failed: {e}")
    exit()

tweet_ids_to_delete = []


for tweet in tweets:
    # Navigate to the 'id' field inside the nested 'tweet' dictionary
    tweet_id = tweet.get("tweet", {}).get("id")
    if tweet_id:
        try:
            api.destroy_status(tweet_id)
            print(f"Deleted tweet {tweet_id}")
        except Exception as e:
            print(f"Error deleting tweet {tweet_id}: {e}")
    else:
        print("Tweet ID is missing.")
