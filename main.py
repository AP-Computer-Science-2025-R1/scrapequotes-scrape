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

from main2 import get_quotes, quotes_date, load_quotes_from_disk, rando_quote
# ==================================
# SECTION 2: FUNCTION DEFINITIONS
# ==================================

# --- Function for Student A ---
# TODO: Put your scrape_all_quotes function here.
# This function should scrape all quotes from the website.
# It should return a list of quote dictionaries.







# --- Function for Student B ---
# TODO: Put your save_quotes_to_disk function here.
# This function should take the list of quotes and a filename.
# It should save the quotes to a JSON or CSV file.



# --- Function for Student C ---
# TODO: Put your load_quotes_from_disk function here.
# This function should take a filename.
# If the file exists, it returns the list of quotes from the file.
# If the file does not exist, it returns an empty list [].

 



# --- Function for Student D ---
# TODO: Put your get_quotes_by_tag function here.
# This function should take the list of quotes.
# It asks the user for a tag and prints any matching quotes.



# --- Function for Student E ---
# TODO: Put your get_random_quote function here.
# This function should take the list of quotes.
# It picks one random quote and prints it.


# ==================================
# SECTION 3: MAIN PROGRAM
# ==================================


# Team Lead/Integrator: Write the main logic here that calls the functions.
if __name__ == "__main__":
    date_str = input("Enter the date (Ex:MM-DD-YYYY): ")
    
    # Scrape all quotes from the website

    scraped_quotes = get_quotes()

    # Save with the same filename pattern
    quotes_date(scraped_quotes, date_str)

    # Load the same file you just saved
    loaded_quotes = load_quotes_from_disk(f"quotes_{date_str}.csv")

    # Show random quote
    rando_quote()

print("-" * 50)
print("Group: Scrape")
print("Members and Contributions:")
print("Edvino Teyuca/Santiago Betancourt, Function: scraped_quotes")
print("Brian Santos Cruz, Function: saved_quotes_to_disk")
print("Valerie Maget/Shejla Osmanovic, Function: load_quotes_from_disk")
print("Robin Ivan Rafael, Function: random_quote_selection")
print("Andrew Morrobel, Function: group_introduction")
print("")
print("The purpose of this project is to practice and demonstrate our abilites, and to prove our capabilites, as well as showing ourseleves how well we can work togther to accomplish a higher goal, as we scrape a website, for certain infomration being able to save it to a file, and then load it back from the file, and finally select a random quote from the loaded data.")