## This walkthrough is for scraping ingredients from bigoven.com recipes and sending them to Google Sheets

## STEP 1 Download this code:
 BigOven_recipe_scraper_Google.py

## Step 2 **Set Up Google Sheets API**:

**Here’s a step-by-step guide to help you create the credentials for a service account and get everything set up:**
    
   **Step 1: Set Up Google Cloud Project**
    
   1.	**Create a New Project**:
    
   •	Go to the [Google Cloud Console](https://console.cloud.google.com/).
    
   •	Click on the project drop-down and select “New Project”.
    
   •	Name your project and click “Create”.
    
   2.	**Enable Google Sheets API**:
    
   •	In the Google Cloud Console, navigate to “APIs & Services” > “Library”.
    
   •	Search for “Google Sheets API” and click on it.
    
   •	Click “Enable”.
    
   3.	**Create Credentials**:
    
   •	Go to “APIs & Services” > “Credentials”.
    
   •	Click “Create Credentials” and select “Service Account”.
    
   •	Fill in the service account name (e.g., my-service-account) and description.
    
   •	Click “Create and Continue”.
    
   4.	**Set Permissions** (Optional):
    
   •	You can skip setting permissions for now by clicking “Continue”.
    
   5.	**Create Key**:
    
   •	Click “Done” to finish creating the service account.
    
   •	Find your service account in the list, click the email, and go to the “Keys” tab.
    
   •	Click “Add Key” > “Create New Key” and select JSON.
    
   •	This will download a JSON file to your computer. Save this file securely as it contains sensitive information.
    
   **Step 2: Share Your Google Sheet**
    
   1.	**Create a New Google Sheet**:
    
   •	Go to Google Sheets and create a new spreadsheet. Name it “Grocery_List”.
    
   2.	**Share the Google Sheet**:
    
   •	Click the “Share” button in the top-right corner.
    
   •	Share the sheet with the email address of your service account. The email will look something like your-service-account-name@your-project-id.iam.gserviceaccount.com.

## Step 3 Update the Script:

1.	**Install Required Libraries in your mac terminal by pasting this command:**

        pip install gspread oauth2client

Then at the top of the python script, underneath

    import requests
    from bs4 import BeautifulSoup
    
add these two lines of code:

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

## Step 4 Add in File Location to Script:

Go in and change 'path/to/your/credentials.json’ with actual path to json key file

Mine is: /Users/austinwalker/Documents/Pthon/grocery_list_project/grocery-list-430106-858b8154e862.json.

## Step 5 Run Script:

1.	**Execute the Updated Script:**

•	Open the script in Python IDLE or your preferred IDE.

•	Run the script and follow the prompts to enter recipe URLs.

•	Type done when you have entered all the URLs.

2.	**Verify the Grocery List in Google Sheets:**

•	Open your Google Sheet named “Grocery List”.

•	Verify that the ingredients have been added correctly.

**Example of Running the Script**

1.	**Start the Script:**

python BigOven_recipe_scraper_Google.py

2.	**Enter Recipe URLs:**

Please enter the recipe URLs you plan to cook this week (type 'done' to finish):
Recipe URL: [URL]
Recipe URL: done

3.	**Check the Google Sheet:**

•	Open the Google Sheet and confirm the grocery list has been populated.
