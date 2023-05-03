from Project_2_core import Core
import requests


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
    def data_search(field: str, input: any, data: dict) -> dict:
        """
        Searches for a specific value in a dictionary based on a given field.

        :param field: A string representing the field of the selected dictionary to search for.
        :param input: The value to search for, can be any type.
        :param data: A dictionary representing the data to search in.

        Returns:
            A dictionary containing the key and value of the first item in the dictionary with a matching field and value,
            or None if no matches are found.
        """
        for key, value in data.items():
            if value[field] == input:
                return [key, value]
        return None

    
    def airport_name_search(airport_name: str) -> dict:
        """
        Searches for an airport by its name.

        :param airport_name: A string representing the name (or partial name) of the airport to search for.

        Returns:
            A dictionary containing the airport code and information about the requested airport,
            or None if no matches are found.
        """
        for key, value in GetData.airports_by_icao.items():
            if airport_name.lower() in value['name'].lower():
                return [key, value]
        return None
    