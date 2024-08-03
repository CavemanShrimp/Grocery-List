BigOven Recipe Scraper and Google Sheets Integration

This project provides a Python script to scrape recipe ingredients from BigOven.com and save them to a Google Sheet. It is designed to help users compile grocery lists from multiple recipes efficiently.

Features

Scrape ingredients from BigOven recipe URLs.
Compile a grocery list from multiple recipe URLs.
Save the compiled grocery list to a Google Sheet.

#Prerequisites

Python 3.x
Google Cloud Project with Google Sheets API enabled
JSON key file for a Google Service Account

Setup Instructions

Step 1: Clone the Repository
git clone https://github.com/yourusername/BigOvenRecipeScraper.git
cd BigOvenRecipeScraper

Step 2: Set Up Google Sheets API

	1.	Create a New Project:
	•	Go to the Google Cloud Console.
	•	Click on the project drop-down and select “New Project”.
	•	Name your project and click “Create”.
	2.	Enable Google Sheets API:
	•	In the Google Cloud Console, navigate to “APIs & Services” > “Library”.
	•	Search for “Google Sheets API” and click on it.
	•	Click “Enable”.
	3.	Create Credentials:
	•	Go to “APIs & Services” > “Credentials”.
	•	Click “Create Credentials” and select “Service Account”.
	•	Fill in the service account name (e.g., my-service-account) and description.
	•	Click “Create and Continue”.
	4.	Set Permissions (Optional):
	•	You can skip setting permissions for now by clicking “Continue”.
	5.	Create Key:
	•	Click “Done” to finish creating the service account.
	•	Find your service account in the list, click the email, and go to the “Keys” tab.
	•	Click “Add Key” > “Create New Key” and select JSON.
	•	This will download a JSON file to your computer. Save this file securely as it contains sensitive information.
	6.	Share Your Google Sheet:
	•	Create a new Google Sheet named “Grocery List”.
	•	Share the sheet with the email address of your service account. The email will look something like your-service-account-name@your-project-id.iam.gserviceaccount.com.

Step 3: Install Required Libraries

Open Terminal or Command Prompt and run:
pip install gspread oauth2client requests beautifulsoup4

Step 4: Update the Script

	1.	Download the script:
	•	BigOven_recipe_scraper_Google_copy.py
	2.	Update the Path to Your JSON Key File:
	•	Open the downloaded script in your code editor.
	•	Replace 'path/to/your/credentials.json’ with the actual path to your JSON key file.

 creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/austinwalker/Documents/Pthon/grocery_list_project/grocery-list-430106-858b8154e862.json', scope)

 
