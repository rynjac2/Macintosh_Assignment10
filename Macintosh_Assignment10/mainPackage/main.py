# File Name : main.py
# Student Name: Ryan Jacob (Cole is MIA)
# email:  Jacobry@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  04/09/2025
# Course #/Section:  IS4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  This project uses the SpaceX API to retrieve recent launch data, extract relevant information, 
# and save it in CSV format using a Python class-based architecture.
# Citations: https://stackoverflow.com/questions/11936967/text-file-parsing-with-python, https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python

from fetcherPackage.data_fetcher import*

if __name__ == "__main__":
    
    #instantiate the SpaceXClient class
    client = SpaceXClient()  

    #fetch data from the SpaceX API
    raw_data = client.fetch_data()

    #parse the fetched data
    parsed_data = client.parse_data(raw_data)

    #save the parsed data to results.csv
    client.save_to_csv(parsed_data)

    print("Latest SpaceX launches have been saved to results.csv!")


