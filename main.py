from room import Room
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

kitchen.get_description()
#kitchen.describe()

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

sword = Item("Sword")
sword.set_description("long, sharp and glistening with jewels")

kitchen.link_room(dining_hall, "south")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

# dining_hall.get_details()
# print("")
# kitchen.get_details()
# print("")
# ballroom.get_details()

current_room = kitchen
current_item = sword

while True:
    print("\n")
    current_room.get_details()
    current_item.get_details()
    command = input(">")
    current_room = current_room.move(command)
