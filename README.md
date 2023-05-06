# Project-2
Project 2 for CSCI1620 at UNOmaha.
Initial idea from https://github.com/JeanExtreme002/FlightRadarAPI, using parts of their core.py file as Project_2_core.py pointers for URLs.
All other files are my own work.

This python project pulls data from the public facing .json file with 1500 flights and their respective data. It then parses that data and users may query the dictionary to display up to eight flights matching that query.
User then selects a flight and the flight ID is added to a URL to pull specific data about that flight, then displays that data in a user friendly label as well as displaying an image of the specific plane that is conducting the flight.