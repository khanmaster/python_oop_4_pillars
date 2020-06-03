# Polymorphism comes with amazing benefit of being able to override particular attributes or behaviour without affecting the super/parent or base class
# Let's see it in action

from encapsulate_reptile_class_in_snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "ok,... hand me the stretchy pants "

    def contrict(self):
        return " and .... squeeeze..."

    def climb(self):
        return "up we go...."

    def shed_skin(self):
        return "I'm growing out of this now...."
#polymorph_python = Python(Snake)
python_seek_heat = Python.seek_heat('')
print(python_seek_heat)
