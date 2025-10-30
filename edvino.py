import requests
from bs4 import BeautifulSoup
import os
import csv
import json

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



filename = f"quotes_{date_str}.csv"

with open('quotes_date.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_quotes)
    print("Your quotes are saved in the 'quotes_date.csv' file!") 

print(f" Your quotes are saved in '{filename}'!")

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
    

