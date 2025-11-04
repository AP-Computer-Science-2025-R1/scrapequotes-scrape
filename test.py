import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import random

#date_str = input("Enter the date (Ex:MM-DD-YYYY):")  #  Date string for filename
def get_quotes():

    URL = "https://quotes.toscrape.com"
    next_page = "/page/1/"
    scraped_quotes = []  # empty list to store [quote, author] pairs


    while next_page:
        page = requests.get(URL + next_page)
        soup = BeautifulSoup(page.text, "html.parser")

        # Find all quote blocks on the page
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()     # The quote text
            author = quote.find("small", class_="author").get_text()  # The author
            print(f"{text}\n— {author}")
            print("-" * 50)
        
            # Save the quote and author
            scraped_quotes.append([text, author])
    
    # Find the next page link
        next_btn = soup.find("li", class_="next")
        if next_btn:  
            next_page = next_btn.find("a")["href"]
        else:
            next_page = None
    
    return scraped_quotes
    
    print(f"\n Scraped {len(scraped_quotes)} quotes total!")
    print("")
#scraped_quotes = get_quotes()

    # Save quotes to a CSV file
def save_quotes_to_disk(scraped_quotes, date_str):
    filename = f"quotes_{date_str}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:  
        writer = csv.writer(csvfile)
        writer.writerow(["Quote", "Author"]) 
        writer.writerows(scraped_quotes)
        print(f"Your quotes are saved in '{filename}' file!") 
#save_quotes_to_disk(scraped_quotes, date_str)


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

#loaded_quotes = load_quotes_from_disk(f"quotes_{date_str}.csv")
#print(f"Loaded {len(loaded_quotes)} quotes from disk.")
#print("")


def get_random_quote(scraped_quotes):
    oratrice = input(str("Would you like a random quote? \n yes or no?"))
    if oratrice =="yes":
        rando_quote = random.choice(scraped_quotes)
        print(rando_quote)

def group_introduction():
    print("-"*50)
    print( "Group: Scrape")
    print("Members and Contributions:")
    print("Edvino Teyuca/Santiago Betancourt, Function: scraped_quotes")
    print("Brian Santos Cruz, Function: saved_quotes_to_disk")
    print("Valerie Maget/Shejla Osmanovic, Function: load_quotes_from_disk")
    print("Robin Ivan Rafael, Function: random_quote_selection")
    print("Andrew Morrobel, Function: group_introduction")
    print("")
    print("The purpose of this project is to practice and demonstrate our abilites, and to prove our capabilites, as well as showing ourseleves how well we can work togther to accomplish a higher goal, as we scrape a website, for certain infomration being able to save it to a file, and then load it back from the file, and finally select a random quote from the loaded data.")
    date_str = input("Enter the date (Ex:MM-DD-YYYY):") 
    return date_str 

date_str = group_introduction()

scraped_quotes = get_quotes()

save_quotes_to_disk(scraped_quotes, date_str)

print(f"Loaded {len(loaded_quotes)} quotes from disk.")

get_random_quote(scraped_quotes)