import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Fetch ingredients from BigOven
def fetch_ingredients_bigoven(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find ingredients section
    ingredients_section = soup.find('div', class_='ingredients')
    if ingredients_section:
        ingredients = ingredients_section.find_all('span', class_='ingredient')
        ingredients_list = [ingredient.get_text().strip() for ingredient in ingredients]
    else:
        ingredients_list = []
    
    return ingredients_list

# Fetch recipe ingredients based on the URL
def fetch_recipe_ingredients(url):
    if 'bigoven.com' in url:
        return fetch_ingredients_bigoven(url)
    else:
        raise ValueError(f"Unsupported website: {url}")

# Compile the grocery list from multiple recipe URLs
def get_grocery_list(recipe_urls):
    grocery_list = []
    for url in recipe_urls:
        try:
            ingredients = fetch_recipe_ingredients(url)
            grocery_list.extend(ingredients)
        except Exception as e:
            print(f"Failed to fetch ingredients from {url}: {e}")
    return grocery_list

# THIS IS WHERE YOU CHANGE TO YOUR HOME DIRECTORY
# Add the grocery list to Google Sheets
def add_to_google_sheets(grocery_list):
    # Google Sheets API setup
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Open the spreadsheet and add data
    sheet = client.open("Grocery List").sheet1  # Open the "Grocery List" spreadsheet and select the first sheet
    sheet.clear()  # Clear existing content
    
    # Add headers
    sheet.append_row(["Ingredient"])
    
    # Add grocery list items
    for ingredient in grocery_list:
        sheet.append_row([ingredient])
    
    print("Grocery list added to Google Sheets.")

# Main function to run the script
def main():
    recipe_urls = []
    print("Please enter the recipe URLs you plan to cook this week (type 'done' to finish):")
    while True:
        url = input("Recipe URL: ")
        if url.lower() == 'done':
            break
        recipe_urls.append(url)
    
    grocery_list = get_grocery_list(recipe_urls)
    
    # Add the grocery list to Google Sheets
    add_to_google_sheets(grocery_list)
    
    print("\nGrocery List:")
    for ingredient in grocery_list:
        print(f"- {ingredient}")

if __name__ == "__main__":
    main()
