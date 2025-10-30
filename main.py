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
import requests
import json
import random
from bs4 import BeautifulSoup
import os
import csv
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

#def- creates a reusable block of the code like a function
def load_quotes_from_disk(filename):
	# os- built in library that interacts with the operating system
	# path- getting the filename
	# exists- to check if the path exists
    if not os.path.exists(filename):
        print("File not found")
		# [] represents an empty list
        return []

    try:
		# filename.endswith .json or .csv- sees if the true/false and can run
        if filename.endswith(".json"):
			# r- reads the file
			# as f- gives it a temporary name to refer to it
			# with- it opens and automatically closes the file
            with open(filename, "r") as f:
                data = json.load(f)
                print("Loaded quotes from JSON file.")
				# exits the function and sends the data to the function
                return data

        elif filename.endswith(".csv"):
            with open(filename, "r") as f:
				# dictreader- turning it into a list
                reader = csv.DictReader(f)
				#list- a way that converts everthing to be organized
                data = list(reader)
                print("Loaded quotes from CSV file.")
                return data

        else:
            print("File type not supported. Use JSON or CSV.")
            return []
# except- tells the program that if there is an error to not stop the whole program but instead handle it on its own
# exception- it catches the errors then prints out the error message
    except Exception as e:
        print("Error reading the file:", e)
        return []


# Example use
if __name__ == "__main__":
    # Example data (you can replace this with your real quotes)
    sample_quotes = [
        {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
        {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"}
	]
# a filename that is present should be inputted what it says "file"
print(load_quotes_from_disk('file'))

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
# if __name__ == "__main__":
