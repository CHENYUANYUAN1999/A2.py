from place import Place
import csv


class PlaceCollection(Place):
    def __init__(self, places=None):
        super().__init__()
        if places is None:
            self.places =[]
        else:
            self.places = places

    def __repr__(self):
        return str(self.places)

    def load_places(self,file):
        with open(file,"r") as csvfile:
            reader = csv.reader(csvfile)
            self.places = list(reader)
            for place in self.places:
                place[2] = int(place[2])
                if place[3] == "n":
                    place[3] = "Unvisited"
                elif place[3] == "v":
                    place[3] = "Visited"
            return self.places

    def save_file(self,file):
        with open(file,"w",newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.places)
        print("Your file has been updated and saved!")

    def add_place(self,location):
        new_list = [location.name, location.country, location.priority, location.check_visited()]
        self.places.append(new_list)
        return self.places

    def sort_by_priority(self,sort_list):
        """sort the list based on the priority"""
        from operator import itemgetter
        sort_list.sort(key=itemgetter(2))
        return sort_list

    def sort_by_alpha(self,sort_list):
        """sort the list in alpha order"""
        sort_list.sort()
        return sort_list

    def sort_by_visit_status(self,sort_list):
        """sort the list according to vistied or not"""
        from operator import itemgetter
        sort_list.sort(key=itemgetter(3),reversed=False)
        return sort_list


    pass
