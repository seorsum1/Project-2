from Project_2_core import Core
from typing import List
import requests

"""
Project 2 for CSCI1620 at UNOmaha.
Initial idea from https://github.com/JeanExtreme002/FlightRadarAPI, using their core.py file as Project_2_core.py pointers for URLs
Project_2.py is all my own work
"""

class GetData(object):
    """
    A class for retrieving flight and airport data from the Flightradar24 API.
    """
    
    flights_request = requests.get(Core.real_time_flight_tracker_data_url, headers=Core.json_headers)
    flights: dict = flights_request.json()
    del flights['full_count']
    del flights['version']
    
    airports_request = requests.get(Core.airports_data_url, headers=Core.json_headers)
    airports: dict = airports_request.json()
    del airports['version']
    airports = airports['rows']
    airports_by_icao: dict[str, dict[str, str]] = {item['icao']: item for item in airports}
    
    def get_flight_info(flight_id: str) -> dict:
        """
        Retrieves information on a specific flight from the Flightradar24 API.

        :param flight_id: A string representing the ID of the flight to retrieve information for.

        Returns:
        A dictionary containing information about the requested flight.
        """
        
        flight_url = Core.flight_data_url + flight_id
        flight_request = requests.get(flight_url)
        flight_info: dict = flight_request.json()
        return flight_info

    
class SearchData(object):
    """
    A class for searching flight and airport data obtained from the Flightradar24 API.
    """
    def data_search(field: str, input: any, data: dict[str, list]) -> dict:
        """
        Searches for a specific value in a dictionary based on a given field.

        :param field: A string representing the field of the selected dictionary to search for.
        :param input: The value to search for, can be any type.
        :param data: A dictionary representing the data to search in.

        Returns:
            A dictionary containing all items in the dictionary with a matching field and value, where the keys are the
        original dictionary keys and the values are the corresponding values of the matching items. Returns an empty
        dictionary if no matches are found.
        """
        results = {}
        for key, value in data.items():
            if value[field] == input:
                results[key] = value
        return results

    
    def airport_name_search(airport_name: str) -> dict:
        """
        Searches for all airports whose name contains a given string.
        
        :param airport_name: A string representing the name (or partial name) of the airport to search for.

        Returns:
            A dictionary containing all airports whose name contains the specified string,
        where the keys are the airport codes and the values are the information about the airports.
        Returns an empty dictionary if no matches are found.
        """
        results = {}
        for key, value in GetData.airports_by_icao.items():
            if airport_name in value['name']:
                results[key] = value
        return results
    
    def flights_list(flights_dict):
        flights_list = [(key, value) for key, value in flights_dict.items()]
        ordered_list = []
        for tuple in flights_list:
            ordered_list.append([tuple[0], tuple[1][16], tuple[1][18], tuple[1][11], tuple[1][12], tuple[1][9], tuple[1][8], tuple[1][1], tuple[1][2], tuple[1][4], tuple[1][3], tuple[1][5]])
        return ordered_list

    
# flight = SearchData.data_search(Core.flights_header['callsign'], '',GetData.flights)

# list2 = (SearchData.flights_list(flight))
# print(type(list2))

# list1 = list(flight.keys())
# flight_info = GetData.get_flight_info(list1[0])
# print(flight_info.keys())
