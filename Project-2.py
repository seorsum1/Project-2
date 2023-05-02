from FlightRadar24.api import FlightRadar24API
from typing import Dict, List

fr_api = FlightRadar24API()

airports = fr_api.get_airports()
airlines = fr_api.get_airlines()
zones = fr_api.get_zones()


def select_zone(large: str = True, medium: str = None, small: str = None) -> List[int]:
    '''
    Returns: 
        List of coordinates for input zone
    :param large: europe, northamerica, southamerica, oceania, asia, africa, atlantic, maldives, northatlantic
    :param medium: poland, germany, uk, spain, france, ceur, scandinavia, italy, na_n, na_c, na_s, japan
    :param small: london, ireland, na_cny, na_cla, na_cat, na_cse, na_nw, na_ne, na_sw, na_se, na_cc
    '''
    if small:
        zone = fr_api.get_bounds(zone=zones[large]['subzones'][medium]['subzones'][small])
    elif medium:
        zone = fr_api.get_bounds(zone=zones[large]['subzones'][medium])
    else:
        zone = fr_api.get_bounds(zone=zones[large])
    return zone


def get_flights(airline_icao: str = None, aircraft_type: str = None, bounds: int = None, aircraft_registration: str = None) -> List[str]:
    """
    Returns:
        List of flights for input data
    :param airline_icao: the airline ICAO. Ex: "DAL"
    :param aircraft_type: aircraft model code. Ex: "B737"
    :param bounds: coordinates (y1, y2 ,x1, x2). Ex: "75.78,-75.78,-427.56,427.56, get from select_zone()"
    :param aircraft_registration: aircraft registration
    """
    flights = fr_api.get_flights(airline=airline_icao, aircraft_type=aircraft_type, bounds=bounds, registration=aircraft_registration)
    return flights

print(get_flights())