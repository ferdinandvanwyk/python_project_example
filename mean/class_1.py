"""
.. module:: Car
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Ferdinand van Wyk <ferdinandvwyk@gmail.com>

"""

class Car():
    """This class defines the Car.
    """

    is_new = True

    def __init__(self, model, year, colour):
        """A really simple class.

        Args:
           model (str): Model of the car.
           year (int): Year of car.
           colour (str): Color of car.

        Kwargs:
           bar (str): Really, same as foo.

        """
        self.model = model
        self.year = year
        self.colour = colour

    def condition(self, name):
        """This function returns the condition of the Car instance.

        Args:
           name (str):  Some test argument.

        Returns:
           str.  The return code::

              "New" -- The car is new.
              "Used" -- The car is used.
        """
        if self.is_new:
            return "New"
        else:
            return "Used"

    def drive(self):
        self.is_new = False

    def description(self, name):
        """This function prints the description of the car instance.

        :param name: Some test argument.
        :type name: str.
        :returns:  str -- the return code.
        :raises: AttributeError, KeyError

        """
        print("This %s was made in %s. It is %s and its condition is %s." 
              %(self.model, self.year, self.colour, self.condition('test')))

