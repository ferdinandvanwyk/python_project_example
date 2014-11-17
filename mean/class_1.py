class Car():

    is_new = True

    def __init__(self, model, year, colour):
        self.model = model
        self.year = year
        self.colour = colour

    def condition(self):
        if self.is_new:
            return "New"
        else:
            return "Used"

    def drive(self):
        self.is_new = False

    def description(self):
        print("This %s was made in %s. It is %s and its condition is %s." 
              %(self.model, self.year, self.colour, self.condition()))

prius = Car("Prius", "2004", "white")
prius.description()
prius.drive()
prius.description()

