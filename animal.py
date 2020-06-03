# These are the four key principle of development
# We will look investigate each of them now

# Let's start with ABSTRACTION by creating a class called Animal

#
class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return " keep on breathing... s"

    def eat(self):
        return "nom nom nom ... nom :"

    def sleep(self):
        return "DO NOT DISTURB I AM SLEEPING"

    def move(self):
        return "backwords upwords and ownwards"

# here we have 4 methods in Animal class which if we instantiate an animal, let's say a cat will now have all these methods.

cat = Animal()
# Let's abstract breathing method from Animal class for cat
#print(cat.sleep())

# breathing is now abstracted the user does not know how breath is implemented, how it works but they can use the method to achievge taking a breathe

# cat can also abstract all other methods if needed from Animal class

#print("cat is eating at the moment " + cat.eat()+ " cat is on the go "+cat.move())

# Let's move onto inheritance - we'll create a new file called reptile and inherite Animal class