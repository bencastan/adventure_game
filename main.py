from room import Room
from item import Item
from character import Enemy, Friend

backpack = []

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

kitchen.get_description()
# kitchen.describe()

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

cheese = Item("cheese")
cheese.set_description("A stinky block of cheese")
kitchen.set_item(cheese)

tiara = Item("tirara")
tiara.set_description("A shiny head piece suitable for a princess")
ballroom.set_item(tiara)

# dining_hall.get_details()
# print("")
# kitchen.get_details()
# print("")
# ballroom.get_details()

dead = False
current_room = kitchen
current_item = sword

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("I eat your brains")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

baxter = Enemy("Baxter", "A rabid wild dog beast")
baxter.set_conversation("Woof Woof")
baxter.set_weakness("tennis")
kitchen.set_character(baxter)

claire = Friend("Claire", "A sexy ghost who loves you")
claire.set_conversation("Come and give me a great big hug")
claire.set_strength("bff")
ballroom.set_character(claire)

while not dead:
    print("\n")
    # Print out the room details
    current_room.get_details()
    # Print out the item/s in the room
    current_item.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        item.describe()
    # Move to another room
    command = input(">")
    if command in ("north", "south", "east", "west"):
        current_room = current_room.move(command)
    # Talk to the inhabitant if they exist in the room
    elif command == "talk":
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            # The inhabitant does not have a lot to say back to you, they are a zombie after all
            say = "What would you like to say to " + inhabitant.get_name() + "?: "
            print(say)
            input(">")
            inhabitant.talk()
        else:
            print("No one else is here!")
            print("Do you always talk to yourself ??")
    elif command == "fight":
        print("What is your weapon of choice ?:")
        fight_with = input(">").lower()
        if not inhabitant.fight(fight_with):
            dead = True

    elif command == "hug":
        if isinstance(inhabitant, Friend):
            strength = inhabitant.get_strength()
            inhabitant.hug(strength)
        elif isinstance(inhabitant, Enemy):
            print(inhabitant.get_name() + " Is a fighter, not a hugger! ")


    # elif command == "fight":
    #	fight_with = input("What will you fight wit?: ")
	#	if self.fight(fight_with) == True:
	#		print("You win")
	#	else:
	#		print("You are now dead")
	#		break

	# current_room = current_room.move(command)
	# dave.talk()
