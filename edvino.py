import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import random

date_str = input("Enter the date:")  # Example date string for filename
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

print(f"\n Scraped {len(scraped_quotes)} quotes total!")


# Save quotes to a CSV file
filename = f"quotes_{date_str}.csv"

with open('quotes_date.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_quotes)
    print("Your quotes are saved in the 'quotes_date.csv' file!") 

print(f" Your quotes are saved in '{filename}'!")


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
                data = list(reader)  # list() makes it organized
                print("Loaded quotes from CSV file.")
                return data
        else:
            print("File type not supported. Use JSON or CSV.")
            return []

    # except - handles any errors without crashing the program
    except Exception as e:
        print("Error reading the file:", e)
        return []

loaded_quotes = load_quotes_from_disk(f"quotes_{date_str}.csv")
print(f"Loaded {len(loaded_quotes)} quotes from disk.")