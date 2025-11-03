

import requests
from bs4 import BeautifulSoup
import os
import csv
import random

# ==================================
#      Python Quote Scraper
#
# Team: [Your Team Name]
# Members: [List of team member names]
# ==================================
single_quote = {
  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
  'author': 'Albert Einstein',
}

multi_quote = [
  
	{
	  'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
	  'author': 'Albert Einstein',
	},
	{
		'text': 'fail. fail. fail. Wow, I just learned 3 new ways on how not to do something!',
		'author': 'Amaurys Valdez',
	},
	{
		'text': 'I Am Groot',
		'author': 'Groot',
	},
]
# SECTION 1: IMPORTS
# All team members: Add the libraries you need for your function here.

import os
import csv
import json
import random
from bs4 import BeautifulSoup
import requests
# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

# --- Function for Student A ---
# TODO: Put your scrape_all_quotes function here.
# This function should scrape all quotes from the website.
# It should return a list of quote dictionaries.
def get_quotes():
    
    URL = "https://quotes.toscrape.com"
    next_page = "/page/1/"
    scraped_quotes = [] 

    while next_page:
        page = requests.get(URL + next_page)
        soup = BeautifulSoup(page.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()     # The quote text
            author = quote.find("small", class_="author").get_text()  # The author
            print(f"{text}\n— {author}")
            print("-" * 50)
            scraped_quotes.append([text, author])

        next_btn = soup.find("li", class_="next")
        if next_btn:  
            next_page = next_btn.find("a")["href"]
        else:
            next_page = None

    print(f"\nScraped {len(scraped_quotes)} quotes total!\n")
    return scraped_quotes  #  Return this list so it can be used later






# --- Function for Student B ---
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.
def quotes_date(scraped_quotes, date_str):
    filename = f"quotes_{date_str}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(scraped_quotes)
        print(f"Your quotes are saved in '{filename}' file!")


# --- Function for Student C ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].
def load_quotes_from_disk(filename):
    # os - built-in library that interacts with the operating system
    # path - getting the filename
    # exists - to check if the path exists
    if not os.path.exists(filename):
        print("File not found.")
        return []  # [] represents an empty list

    try:
        if filename.endswith(".csv"):
            with open(filename, "r", encoding="utf-8") as f:
                # DictReader - turns each row into a dictionary
                reader = csv.DictReader(f)
                data = list(reader)
                print("Loaded quotes from CSV file.")
                return data
        else:
            print("File type not supported. Use JSON or CSV.")
            return []

    # except - handles any errors without crashing the program
    except Exception as e:
        print("Error reading the file:", e)
        return []

date_str = input("Enter the date (Ex:MM-DD-YYYY):")
loaded_quotes = load_quotes_from_disk(f"quotes_{date_str}.csv")
print(f"Loaded {len(loaded_quotes)} quotes from disk.")
print("")




# --- Function for Student D ---
# TODO: Put your get_quotes_by_tag function here.
# This function should take the list of quotes.
# It asks the user for a tag and prints any matching quotes.



# --- Function for Student E ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.
def rando_quote():
    oratrice = input(str("Would you like a random quote? \n yes or no?"))
    if oratrice == "yes":
        rando_quote = random.choice(scraped_quotes)
        print(rando_quote)

if __name__ == "__main__":
    