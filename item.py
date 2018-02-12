class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.rooms = {}

    def set_description(self, item_description):
        self.description = item_description

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_details(self):
        print("You have a {} which is {}".format(self.get_name(), self.get_description()))
