import random
import csv

According_to_the_oratrice_mechanique_danalyse_cardinale = input(str("Would you like a random quote? \n yes or no?"))
 if According_to_the_oratrice_mechanique_danalyse_cardinale == "yes":
    rando_quote = random.choice(scraped_quotes)
    print rando_quote