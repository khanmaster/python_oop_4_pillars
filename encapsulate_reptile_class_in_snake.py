# Encapsulation relates to hiding certain details from users

from inherite_animal_into_reptile import *

# Let's create Snake class and encapsulate Reptile class with in

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        tongue = self.forked_tongue
        self.cold_blooded = True
        self.venom = True
        self.limbs - False

    def use_tongue_to_smell(self):
        return " Do I say it smells or tastes nice...?"

# if we instantiate our snake class

#cobra = Snake()?
# print(Snake.use_tongue_to_smell('') + " " + Snake.seek_heat(''))

# Now we have double inheritance from Animal, reptile and Snake inheriting from the previous 2 classess!
# However if we wanted to encapsulate (make private) the seek heat we could essentially hide the method with an underscore _

# moving onto Pylymorphsim - create a new file