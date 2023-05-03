from abc import ABC


class Core(ABC):
    """
    Base class for Flightradar24 API requests.
    Source is https://github.com/JeanExtreme002/FlightRadarAPI/core.py
    This class defines the base URLs and headers for HTTP requests to the Flightradar24 API.
    """


    # Base URLs.
    cdn_flightradar_base_url: str = "https://cdn.flightradar24.com"
    flightradar_base_url: str = "https://www.flightradar24.com"
    data_live_base_url: str = "https://data-live.flightradar24.com"

    # Flights data URLs.
    real_time_flight_tracker_data_url: str = data_live_base_url + "/zones/fcgi/feed.js"
    flight_data_url: str = data_live_base_url + "/clickhandler/?flight="
    
    # Airports data URLs.
    airport_data_url: str = flightradar_base_url + "/airports/traffic-stats/?airport="
    airports_data_url: str = flightradar_base_url + "/_json/airports.php"

    # Airlines data URL.
    airlines_data_url: str = flightradar_base_url + "/_json/airlines.php"

    # Zones data URL.
    zones_data_url: str = flightradar_base_url + "/js/zones.js.php"

    # Country flag image URL.
    country_flag_url: str = flightradar_base_url + "/static/images/data/flags-small/{}.gif"

    # Airline logo image URL.
    airline_logo_url: str = cdn_flightradar_base_url + "/assets/airlines/logotypes/{}_{}.png"
    alternative_airline_logo_url: str = flightradar_base_url + "/static/images/data/operators/{}_logo0.png"

    headers: dict[str, str] = {
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

    json_headers: dict[str, str] = headers.copy()
    json_headers["accept"] = "application/json"

    image_headers: dict[str, str] = headers.copy()
    image_headers["accept"] = "image/gif, image/jpg, image/jpeg, image/png"
    
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
