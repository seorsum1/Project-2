from abc import ABC


class Core(ABC):
    """
    Base class for Flightradar24 API requests.
    Source is https://github.com/JeanExtreme002/FlightRadarAPI/core.py
    This class defines the base URLs and headers for HTTP requests to the Flightradar24 API.
    """

    # Base URL.
    data_live_base_url: str = "https://data-live.flightradar24.com"

    # Flights data URLs.
    real_time_flight_tracker_data_url: str = data_live_base_url + "/zones/fcgi/feed.js"
    flight_data_url: str = data_live_base_url + "/clickhandler/?flight="
    
    json_headers: dict[str, str] = {
        "accept": "application/json",
        "accept-encoding": "gzip, br",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "origin": "https://www.flightradar24.com",
        "referer": "https://www.flightradar24.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    # Dictionary to point query to correct index location
    flights_header: dict[str, int] = {
        "icao_24bit" : 0,
        "latitude" : 1,
        "longitude" : 2,
        "heading" : 3,
        "altitude" : 4,
        "ground_speed" : 5,
        "squawk" : 6,
        "aircraft_code" : 8,
        "registration" : 9,
        "time" : 10,
        "origin_airport_iata" : 11,
        "destination_airport_iata" : 12,
        "on_ground" : 14,
        "vertical_speed" :15,
        "callsign" : 16,
        "airline_icao" : 18,
    }

    # Latitudes and longitudes for location based filter
    locations: dict[str, list[float]] = {
        #"Location" : ['lat1', 'lon1', 'lat2', 'lon2'],
        "Nebraska": [42.921, -103.99, 40.001, -95.314],
        "North America": [68.931, -169.176, 15.435, -63.781],
        "Europe": [66.417, -27.452, 35.038, 35.709],
        "Asia": [52.611, 78.789, -11.687, 154.112],
    }