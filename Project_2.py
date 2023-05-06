import sys, requests
from Project_2_core import Core
from Project_2_func import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
from Project_2_UI import Ui_MainWindow
from typing import List, Dict, Any


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect submit_button to search and display functions
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
        MainWindow.reset_results_labels(self)
        
        field = self.ui.field_dropdown.currentText()
        query = self.ui.query_entry.text()
        location = self.ui.location_checkBox
        area = self.ui.location_dropdown.currentText()
        
        if not query:
            self.show_error_message('Please enter a query')
        elif not field:
            self.show_error_message('Please select a field to query')
        elif location.isChecked() and area == '':
                self.show_error_message('Please select a location to filter by')
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

            if self.ui.whole_checkBox.isChecked():
                results_dict: Dict[str, List[Any]] = SearchData.whole_search(Core.flights_header[data_search_key], query, GetData.flights)
            else:
                results_dict: Dict[str, List[Any]] = SearchData.partial_search(Core.flights_header[data_search_key], query, GetData.flights)
            ordered_list: List[Any] = SearchData.flights_list(results_dict)

            if not ordered_list:
                MainWindow.reset_results_labels(self)
                self.ui.flight_data_label.setText("No results, please try again")
            else:
                if location.isChecked():
                    bounds: List[float] = Core.locations[area]
                    ordered_list = [flight for flight in ordered_list if ((bounds[0] < flight[7] < bounds[2]) or (bounds[0] > flight[7] > bounds[2])) and ((bounds[1] < flight[8] < bounds[3]) or (bounds[1] > flight[8] > bounds[3]))]

            
                for i in range(len(ordered_list) if len(ordered_list) < 8 else 8):
                    label_name = f"results_label_{i+1}"
                    label_text = "{:<10}".format(ordered_list[i][1]) + "|" + "{:^11}".format(ordered_list[i][2]) + "|" + "{:^10}".format(ordered_list[i][3]) + "|" + "{:^8}".format(ordered_list[i][4]) + "|" + "{:^12}".format(ordered_list[i][5]) + "|" + "{:^10}".format(ordered_list[i][6]) + "|" + "{:^8}".format("{:.3f}".format(ordered_list[i][7])) + "|" + "{:^9}".format("{:.3f}".format(ordered_list[i][8])) + "|" + "{:^9}".format(ordered_list[i][9]) + "|" + "{:^7}".format(ordered_list[i][10]) + "|" + "{:^7}".format(ordered_list[i][11]) + "|"
                    label = getattr(self.ui, label_name)
                    label.setText(label_text)
                    label_name = f"flight_button_{i+1}"
                    label_text = ordered_list[i][0]
                    label = getattr(self.ui, label_name)
                    label.setText(label_text)
   
    def display_flight_info(self, flight: int) -> None:
        button_flight_id = f"flight_button_{flight}"
        flight_button_label = getattr(self.ui, button_flight_id)
        flight_id = flight_button_label.text()
        data = GetData.get_flight_info(flight_id)
        # Populate flight_info_label with flight information
        if data.get('identification') is not None:
            if data['identification'].get('callsign') is not None:
                callsign = data['identification'].get('callsign', '')
            else:
                callsign = ''
        else:
            callsign = ''

        if data.get('aircraft') is not None:
            if data['aircraft'].get('registration') is not None:
                registration = data['aircraft'].get('registration', '')
            else:
                registration = ''
            if data['aircraft'].get('model') is not None:
                aircraft_type = data['aircraft']['model'].get('text', '')
            else:
                aircraft_type = ''    
        else:
            registration = ''
            aircraft_type = ''

        if data.get('airline') is not None:
            if data['airline'].get('name') is not None:
                airline = data['airline'].get('name', '')
            else:
                airline = ''
        else:
            airline = ''

        if data.get('airport') is not None:
            if data['airport'].get('origin') is not None:
                origin = data['airport']['origin'].get('name', '')
            else:
                origin = ''
            if data['airport'].get('destination') is not None:
                destination = data['airport']['destination'].get('name', '')
            else:
                destination = ''   
        else:
            origin = ''
            destination = ''

        if data.get('trail') is not None and len(data['trail']) > 0:
            if data['trail'][0].get('alt') is not None:
                altitude = data['trail'][0].get('alt', '')
            else:
                altitude = ''
            if data['trail'][0].get('spd') is not None:
                speed = data['trail'][0].get('spd', '')
            else:
                speed = ''
            if data['trail'][0].get('hd') is not None:
                heading = data['trail'][0].get('hd', '')
            else:
                heading = ''
        else:
            altitude = ''
            speed = ''
            heading = ''
        text_to_display = f"Callsign: {callsign}\nRegistration: {registration}\nAircraft Type: {aircraft_type}\nAirline: {airline}\nOrigin: {origin}\nDestination: {destination}\nAltitude: {altitude}\nSpeed: {speed}\nHeading: {heading}"
        self.ui.flight_data_label.setText(str(text_to_display))
        
        # Show Image of plane
        try:
            url = data['aircraft']['images']['medium'][0]['src']
            request = requests.get(url)
            image_data = request.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.ui.image_label.setPixmap(pixmap)
            self.show()
        except:
            self.ui.image_label.setText('No image to display')
        
    
    def reset_results_labels(self) -> None:
        self.ui.image_label.setPixmap(QPixmap(0, 0))
            
        for i in range(8):
            label_name = f"results_label_{i+1}"
            label_text = ""
            label = getattr(self.ui, label_name)
            label.setText(label_text)

        for i in range(8):
            label_name = f"flight_button_{i+1}"
            label_text = f"Flight {i+1}"
            label = getattr(self.ui, label_name)
            label.setText(label_text)
            
    def show_error_message(self, msg):
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