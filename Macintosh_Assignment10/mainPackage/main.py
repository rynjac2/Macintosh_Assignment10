# File Name : main.py
# Student Name: Cole Crooks
# email:  crookscl@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:  04/09/2025
# Course #/Section:  IS4010-002
# Semester/Year:  Spring 2025
# Brief Description of the assignment:  This project uses the SpaceX API to retrieve recent launch data, extract relevant information, 
# and save it in CSV format using a Python class-based architecture.
# This module contains the SpaceXClient class, which handles API requests, parses launch data, and writes selected information to a CSV file.
# Citations:

from fetcherPackage.data_fetcher import*

if __name__ == "__main__":

    def main():
        client = SpaceXClient()

        print("Fetching SpaceX launch data...")
        try:
            raw_data = client.fetch_data()
            print(f"Fetched {len(raw_data)} launch records.")
        except Exception as e:
            print(f"Failed to fetch data: {e}")
            return
        try:
            client.save_to_csv(client.parse_data(raw_data, limit=10))
            print("Latest SpaceX launches have been saved to results.csv!")
        except Exception as e:
            print(f"Failed to save data: {e}")

    if __name__ == "__main__":
        main()