import sys, requests
from Project_2_core import Core
from Project_2_func import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from Project_2_UI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
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
    
    def search_and_display(self):
        MainWindow.reset_results_labels(self)
        
        field = self.ui.field_dropdown.currentText()
        query = self.ui.query_entry.text()

        if field == "Airline":
            data_search_key = 'airline_icao'
        elif field == "Aircraft Type":
            data_search_key = 'aircraft_code'
        elif field == "Origin":
            data_search_key = 'origin_airport_iata'
        elif field == "Destination":
            data_search_key = 'destination_airport_iata'
        elif field == "Registration":
            data_search_key = 'registration'

        if field == "Callsign":
            results_dict = SearchData.callsign_search(Core.flights_header[field.lower()], query, GetData.flights)
        else:
            results_dict = SearchData.data_search(Core.flights_header[data_search_key], query, GetData.flights)
        ordered_list = SearchData.flights_list(results_dict)

        if not ordered_list:
            MainWindow.reset_results_labels(self)
        else:
            for i in range(len(ordered_list) if len(ordered_list) < 8 else 8):
                label_name = "results_label_{}".format(i+1)
                label_text = "{:<10}".format(ordered_list[i][1]) + "|" + "{:^11}".format(ordered_list[i][2]) + "|" + "{:^10}".format(ordered_list[i][3]) + "|" + "{:^8}".format(ordered_list[i][4]) + "|" + "{:^12}".format(ordered_list[i][5]) + "|" + "{:^10}".format(ordered_list[i][6]) + "|" + "{:^8}".format("{:.3f}".format(ordered_list[i][7])) + "|" + "{:^9}".format("{:.3f}".format(ordered_list[i][8])) + "|" + "{:^9}".format(ordered_list[i][9]) + "|" + "{:^7}".format(ordered_list[i][10]) + "|" + "{:^7}".format(ordered_list[i][11]) + "|"
                label = getattr(self.ui, label_name)
                label.setText(label_text)
                label_name = "flight_button_{}".format(i+1)
                label_text = ordered_list[i][0]
                label = getattr(self.ui, label_name)
                label.setText(label_text)
   
    def display_flight_info(self, flight):
        button_flight_id = "flight_button_{}".format(flight)
        temp = getattr(self.ui, button_flight_id)
        flight_id = temp.text()
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
        url = data['aircraft']['images']['medium'][0]['src']
        request = requests.get(url)
        image_data = request.content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        self.ui.image_label.setPixmap(pixmap)
        self.show()
    
    def reset_results_labels(self):
        for i in range(8):
            label_name = "results_label_{}".format(i+1)
            label_text = ""
            label = getattr(self.ui, label_name)
            label.setText(label_text)

        for i in range(8):
            label_name = "flight_button_{}".format(i+1)
            label_text = "Flight {}".format(i+1)
            label = getattr(self.ui, label_name)
            label.setText(label_text)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = MainWindow()
    tool.show()
    sys.exit(app.exec_())