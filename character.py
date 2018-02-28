class Character:


    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def get_name(self):
        return self.name


class Enemy(Character):
    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        
        super().__init__(char_name, char_description)
        self.weakness = None

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def set_weakness(self, weakness_item):
        self.weakness = weakness_item

    def get_weakness(self):
        return self.weakness

    def set_enemies_defeated(self, number_defeated):
        Enemy.enemies_defeated = number_defeated

    def get_enemies_defeated(self):
        return Enemy.enemies_defeated


class Friend(Character):

    def __init__(self, char_name, char_description):
        
        super().__init__(char_name, char_description)
        self.strength = None

    def hug(self, strength_item):
        if strength_item == "bff":
            print(self.name + " gives youy a great big hug")
            return True
        elif strength_item == "sm":
            print(self.name + " gives you a hug")
            return True
        elif strength_item == "ff":
            print(self.name + " nods politely to you")
            return True
        else:
            print(self.name + " has no idea who you are")
            return False

    def set_strength(self, strength_item):
        self.strength = strength_item

    def get_strength(self):
        return self.strength