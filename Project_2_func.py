from Project_2_core import Core
from typing import List, Dict, Any
import requests


class GetData:
    """
    A class for retrieving flight and airport data from the Flightradar24 API.
    """
    flights_request = requests.get(Core.real_time_flight_tracker_data_url, headers=Core.json_headers)
    flights: Dict[str, Any] = flights_request.json()
    del flights['full_count']
    del flights['version']
    
    def get_flight_info(flight_id: str) -> Dict[str, Any]:
        """
        Retrieves information on a specific flight from the Flightradar24 API.

        :param flight_id: A string representing the ID of the flight to retrieve information for.

        Returns:
        A dictionary containing information about the requested flight.
        """
        
        flight_url = Core.flight_data_url + flight_id
        flight_request = requests.get(flight_url, headers=Core.json_headers)
        flight_info: Dict[str, Any] = flight_request.json()
        return flight_info

    
class SearchData:
    """
    A class for searching flight and airport data obtained from the Flightradar24 API.
    """
    def whole_search(field: str, input: Any, data: Dict[str, Any]) -> Dict[str, Any]:
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
        return {key: value for key, value in data.items() if input.lower() == value[field].lower()}

    def partial_search(field: str, input: any, data: dict[str, list]) -> dict:
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
        
        return {key: value for key, value in data.items() if input.lower() in value[field].lower()}
    
    def flights_list(flights_dict: Dict[str, Any]) -> List[List[Any]]:
        flights_list = [(key, value) for key, value in flights_dict.items()]
        ordered_list = []
        for flights_tuple in flights_list:
            if flights_tuple[1][8] != 'GLID' and flights_tuple[1][8] != 'BALL':
                ordered_list.append([flights_tuple[0], flights_tuple[1][16], flights_tuple[1][18], flights_tuple[1][11], flights_tuple[1][12], flights_tuple[1][9], flights_tuple[1][8], flights_tuple[1][1], flights_tuple[1][2], flights_tuple[1][4], flights_tuple[1][3], flights_tuple[1][5]])
        return ordered_list