import sys, requests
from Project_2_core import Core
from Project_2_func import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QCheckBox
from PyQt5.QtGui import QPixmap
from Project_2_UI import Ui_MainWindow
from typing import List, Dict, Any
    
"""
Project 2 for CSCI1620 at UNOmaha.
Initial idea from https://github.com/JeanExtreme002/FlightRadarAPI, using parts of their core.py file as Project_2_core.py pointers for URLs.
All other files are my own work.

This python project pulls data from the public facing .json file with 1500 flights and their respective data. It then parses that data and users may query the dictionary to display up to eight flights matching that query.
User then selects a flight and the flight ID is added to a URL to pull specific data about that flight, then displays that data in a user friendly label as well as displaying an image of the specific plane that is conducting the flight.
"""

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initialize MainWindow Class
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect submit button to query function
        self.ui.submit_button.clicked.connect(self.search_and_display)
        
        # Connect flight buttons to display flight info
        self.ui.flight_button_1.clicked.connect(lambda: self.display_flight_info(1))
        self.ui.flight_button_2.clicked.connect(lambda: self.display_flight_info(2))
        self.ui.flight_button_3.clicked.connect(lambda: self.display_flight_info(3))
        self.ui.flight_button_4.clicked.connect(lambda: self.display_flight_info(4))
        self.ui.flight_button_5.clicked.connect(lambda: self.display_flight_info(5))
        self.ui.flight_button_6.clicked.connect(lambda: self.display_flight_info(6))
        self.ui.flight_button_7.clicked.connect(lambda: self.display_flight_info(7))
        self.ui.flight_button_8.clicked.connect(lambda: self.display_flight_info(8))
    
    def search_and_display(self) -> None:
        """
        Searches for and displays results
        """
        
        # Ensure display is starting from default settings
        MainWindow.reset_results_labels(self)
        
        field: str = self.ui.field_dropdown.currentText()
        query: str = self.ui.query_entry.text()
        location: QCheckBox = self.ui.location_checkBox
        area: str = self.ui.location_dropdown.currentText()
        
        # Ensures query has all required fields, displays an error if not
        if not query:
            self.show_error_message('Please enter a query')
        elif not field:
            self.show_error_message('Please select a field to query')
        elif location.isChecked() and area == '':
                self.show_error_message('Please select a location to filter by')
        
        # Sets up query
        else:
            self.ui.flight_data_label.setText("Select a flight to view more infomation!")
            if field == "Callsign":
                data_search_key = 'callsign'
            elif field == "Airline":
                data_search_key = 'airline_icao'
            elif field == "Aircraft Type":
                data_search_key = 'aircraft_code'
            elif field == "Origin":
                data_search_key = 'origin_airport_iata'
            elif field == "Destination":
                data_search_key = 'destination_airport_iata'
            elif field == "Registration":
                data_search_key = 'registration'

            # Changes which function, match whole field or only partial field
            if self.ui.whole_checkBox.isChecked():
                results_dict: Dict[str, List[Any]] = SearchData.whole_search(Core.flights_header[data_search_key], query, GetData.flights)
            else:
                results_dict: Dict[str, List[Any]] = SearchData.partial_search(Core.flights_header[data_search_key], query, GetData.flights)
            ordered_list: List[Any] = SearchData.flights_list(results_dict)

            if not ordered_list:
                MainWindow.reset_results_labels(self)
                self.ui.flight_data_label.setText("No results, please try again")
                MainWindow.hide_flight_buttons(self)
            else:
                # Sets up location based filter
                if location.isChecked():
                    bounds: List[float] = Core.locations[area]
                    ordered_list = [flight for flight in ordered_list if ((bounds[0] < flight[7] < bounds[2]) or (bounds[0] > flight[7] > bounds[2])) and ((bounds[1] < flight[8] < bounds[3]) or (bounds[1] > flight[8] > bounds[3]))]

                # Displays results in each results_label
                for i in range(len(ordered_list) if len(ordered_list) < 8 else 8):
                    label_name: str = f"results_label_{i+1}"
                    label_text: str = "{:<10}".format(ordered_list[i][1]) + "|" + "{:^11}".format(ordered_list[i][2]) + "|" + "{:^10}".format(ordered_list[i][3]) + "|" + "{:^8}".format(ordered_list[i][4]) + "|" + "{:^12}".format(ordered_list[i][5]) + "|" + "{:^10}".format(ordered_list[i][6]) + "|" + "{:^8}".format("{:.3f}".format(ordered_list[i][7])) + "|" + "{:^9}".format("{:.3f}".format(ordered_list[i][8])) + "|" + "{:^9}".format(ordered_list[i][9]) + "|" + "{:^7}".format(ordered_list[i][10]) + "|" + "{:^7}".format(ordered_list[i][11]) + "|"
                    label = getattr(self.ui, label_name)
                    label.setText(label_text)
                    label_name: str = f"flight_button_{i+1}"
                    label_text: str = ordered_list[i][0]
                    label = getattr(self.ui, label_name)
                    label.setText(label_text)
                MainWindow.hide_flight_buttons(self)
   
    def display_flight_info(self, flight: int) -> None:
        """Displays Flight information in lower section of UI

        Args:
            flight (int): 1-8 Selecting which button was pressed to grab the flight ID and process through the URL in Core
        """
        
        
        button_flight_id = f"flight_button_{flight}"
        flight_button_label = getattr(self.ui, button_flight_id)
        flight_id = flight_button_label.text()
        data = GetData.get_flight_info(flight_id)
       
        # Initializing variables in case they are 'None' to prevent errors
        callsign: str = ''
        registration: str = ''
        aircraft_type: str = ''
        airline: str = ''
        origin: str = ''
        destination: str = ''
        altitude: str = ''
        speed: str = ''
        heading: str = ''
        
        # Prepares variables to display data
        if data.get('identification') is not None:
            if data['identification'].get('callsign') is not None:
                callsign = data['identification'].get('callsign', '')

        if data.get('aircraft') is not None:
            if data['aircraft'].get('registration') is not None:
                registration = data['aircraft'].get('registration', '')
            if data['aircraft'].get('model') is not None:
                aircraft_type = data['aircraft']['model'].get('text', '')

        if data.get('airline') is not None:
            if data['airline'].get('name') is not None:
                airline = data['airline'].get('name', '')

        if data.get('airport') is not None:
            if data['airport'].get('origin') is not None:
                origin = data['airport']['origin'].get('name', '')
            if data['airport'].get('destination') is not None:
                destination = data['airport']['destination'].get('name', '')


        if data.get('trail') is not None and len(data['trail']) > 0:
            if data['trail'][0].get('alt') is not None:
                altitude = data['trail'][0].get('alt', '')
            if data['trail'][0].get('spd') is not None:
                speed = data['trail'][0].get('spd', '')
            if data['trail'][0].get('hd') is not None:
                heading = data['trail'][0].get('hd', '')
        
        # Displays variables in user friendly format        
        text_to_display = f"Callsign: {callsign}\nRegistration: {registration}\nAircraft Type: {aircraft_type}\nAirline: {airline}\nOrigin: {origin}\nDestination: {destination}\nAltitude: {altitude}\nSpeed: {speed}\nHeading: {heading}"
        self.ui.flight_data_label.setText(str(text_to_display))
        
        # Shows image of plane
        try:
            url = data['aircraft']['images']['medium'][0]['src']
            request = requests.get(url)
            image_data = request.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.ui.image_label.setPixmap(pixmap)
            self.ui.image_label.show()
        except:
            self.ui.image_label.setText('No image to display')

    def hide_flight_buttons(self) -> None:
        """Hides or shows flight buttons depending if there is a flight ID attached to the button
        """
        for i in range(8):
            label_name: str = f"flight_button_{i+1}"
            label_text: str = getattr(self.ui, label_name).text()
            if label_text == f"Flight {i+1}":
                getattr(self.ui, label_name).setVisible(False)
            else:
                getattr(self.ui, label_name).setVisible(True)
    
    def reset_results_labels(self) -> None:
        """Resets the plane image, flight buttons, and results labels to default settings
        """
        self.ui.image_label.setPixmap(QPixmap())
            
        for i in range(8):
            label_name: str = f"results_label_{i+1}"
            label_text: str = ""
            label = getattr(self.ui, label_name)
            label.setText(label_text)

        for i in range(8):
            label_name = f"flight_button_{i+1}"
            label_text = f"Flight {i+1}"
            label = getattr(self.ui, label_name)
            label.setText(label_text)
            
    def show_error_message(self, msg: str) -> None:
        """Opens error QMessageBox and displays error passed

        Args:
            msg (str): Error message passed to user
        """
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText(msg)
        message_box.setWindowTitle("Error")
        message_box.exec_()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = MainWindow()
    tool.show()
    sys.exit(app.exec_())