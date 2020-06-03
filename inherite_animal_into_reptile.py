# Inheritance is one the key principle of OOP and we will dive straight into how we go about doing it

from animal import Animal
# here we are importing Animal class
# we will review the below code at the end

class Reptile(Animal):
    def __init__(self):
        super.__init__()
        self.cold_blooded = True
        self.tetrapod = None # should be set as not all reptiles are tetrapods..
        self.hear_chamber = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        return "It's chilly outside, where's the sun or a decent hot spring"

    def hunt(self):
        return "wait for it, wait for it...... and bounce"

    def use_venom(self):#
        return "if I have got it I'm using it"
# we created some methods in Reptile class and inherited some from Animal class
# Let's see how can we utilise the inheritance functionality here

#print("on a hunt for food .."+ Reptile.hunt('') + " .. got food " + Reptile.eat('')+ " yumm...")
# cool! we are able to use methods from parent and child class

# Let's move onto Encapsulation - create a new file