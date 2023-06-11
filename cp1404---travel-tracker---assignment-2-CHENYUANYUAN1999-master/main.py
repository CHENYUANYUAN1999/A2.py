"""
Name: Chen YuanYuan
Date: 05/06/2023
Brief Project Description: This program is done based on the A1, create kivi app to present the program
GitHub URL: https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-CHENYUANYUAN1999
"""
# Create your main program in this file, using the TravelTrackerApp class

import csv
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from placecollection import PlaceCollection


class TravelTrackerApp(App):
    bottom_status_text = StringProperty()
    top_status_text = StringProperty()
    current_sort = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        travel_locations = PlaceCollection()
        self.app_list = travel_locations.load_places("places.csv")

    def build(self):
        self.title = "TravelTracker App"
        self.root = Builder.load_file("app.kv")
        self.create_widgets()
        return self.root

    def clear_input(self):
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def create_widgets(self):
        self.bottom_status_text = "Click on a place to change it to visited/unvisited"
        for location in self.app_list:
            if location[3] == "Visited":
                button = Button(text="{} in {}, priority {} ({})".format(location[0],location[1],location[2],location[3]))
            else:
                button = Button(text="{} in {}, priority {}".format(location[0], location[1], location[2]))
            button.bind(on_release=self.press_entry)
            button.location = location
            if location[3] == "Unvisited":
                button.background_color = [0,0,0,1]
            else:
                button.background_color = [0,1,0,1]
            self.root.ids.entry_box.add_widget(button)
        self.count_unvisited_places()

    def press_entry(self,example):
        location = example.location
        if location[3] == "Visited":
            location[3] = "Unvisited"
        else:
            location[3] = "Visited"
        self.root.ids.entry_box.clear_widgets()
        self.create_widgets()

        if self.is_important(location[2]):
            if location[3] == "Visited":
                self.bottom_status_text = "You visited {}. Great travelling".format(location[0])
            elif location[3] == "Unvisited":
                self.bottom_status_text = "You need to visit {}. Get going".format(location[0])

        else:
            if location[3] == "Visited":
                self.bottom_status_text = "You visited {}.".format(location[0])
            elif location[3] == "Unvisited":
                self.bottom_status_text = "You need to visit {}.".format(location[0])

    def add_place(self):
        new_list = []
        try:
            name = self.root.ids.input_name.text
            country = self.root.ids.input_country.text
            priority = int(self.root.ids.input_priority.text)
            if name == "" or country == "" or priority == "":
                self.bottom_status_text = "All fields must be completed"
            elif priority <= 0:
                self.bottom_status_text = "Priority must be > 0"
            elif name.isdigit() and country.isdigit():
                self.bottom_status_text = "Name or Country can not be digit"
            else:
                new_list.append(name)
                new_list.append(country)
                new_list.append(priority)
                new_list.append("Unvisited")
                self.app_list.append(new_list)
                self.root.ids.entry_box.clear_widgets()
                self.create_widgets()
                self.bottom_status_text = "{} has been added.".format(name)
        except ValueError:
            self.bottom_status_text = "Invalid input. Priority must be a valid number."
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def sorted_by_priority(self):
        """insert an ordering function sorted by priority in increasing order"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(2))
        print(self.app_list)
        self.root.ids.entry_box.clear_widgets()
        self.create_widgets()

    def sorted_by_alpha(self):
        """insert an ordering function sorted by alphabet"""
        self.app_list.sort()
        print(self.app_list)
        self.root.ids.entry_box.clear_widgets()
        self.create_widgets()

    def sorted_by_visit_status(self):
        """insert an ordering function sorted by visit status"""
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(3), reverse=False)
        print(self.app_list)
        self.root.ids.entry_box.clear_widgets()
        self.create_widgets()

    def is_important(self,priority):
        """Check the importance according to priority"""
        if priority <= 2:
            return True

    def on_stop(self):
        import csv
        with open("places.csv","w",newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.app_list)

    def count_unvisited_places(self):
        """Calculates the number of visited places in the list."""
        unvisited_count = sum(1 for location in self.app_list if location[3] == "Unvisited")
        self.top_status_text = str(unvisited_count)
        return unvisited_count


TravelTrackerApp().run()
