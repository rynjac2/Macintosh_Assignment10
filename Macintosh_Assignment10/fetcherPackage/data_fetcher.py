# File Name : fetcherPackage/data_fetcher.py
# Student Name: Ryan Jacob
# email:  Jacobry@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  04/09/2025
# Course #/Section:  IS4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  This project uses the SpaceX API to retrieve recent launch data, extract relevant information, 
# and save it in CSV format using a Python class-based architecture.
# This module contains the SpaceXClient class, which handles API requests, parses launch data, and writes selected information to a CSV file.
# Citations: https://stackoverflow.com/questions/11936967/text-file-parsing-with-python, https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python





import requests
import csv
import json

class SpaceXClient:
    def __init__(self):
        self.api_url = "https://api.spacexdata.com/v4/launches"

    def fetch_data(self):
        #This method fetches the data from SpaceX API
        response = requests.get(self.api_url)
        response.raise_for_status()
        # should raise an error if the request was unsuccessful
        return response.json()


       

    def parse_data(self, data, limit=10):
        #This method parses  the fetched data
        parsed = []

        for launch in sorted(data, key=lambda x: x['date_utc'], reverse=True)[:limit]:
            parsed.append({
                'name': launch.get('name'),
                'date': launch.get('date_utc'),
                'status': launch.get('status') or "No status provided",
                'rocket': launch.get('rocket'),
                'mission': launch.get('mission') or "No mission details provided"
            })
        return parsed

    # Save parsed data to results.csv in directory folder
    def save_to_csv(self, parsed_data, filename="results.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=parsed_data[0].keys())
            writer.writeheader()
            writer.writerows(parsed_data)
