from turtle import Turtle
class Racer(Turtle):
    """Racer class which inherits from the Turtle class

    Extends the Turtle class to support more attributes

    """
    def __init__(self, shape, name, col, start_pos_x, start_pos_y):
        """
        Constructor of the Racer class object.
        Includes the __init__ function of the Turtle class to inherit from it
        :param name: the name of the racer
        :param col: the colour of the racer
        :param start_pos_x: the starting position of the racer in the x axis
        :param start_pos_y: the starting position of the racer in the y axis
        """
        Turtle.__init__(self, shape=shape)
        self.name = name
        self.col = col
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

    def __str__(self):
        """
        Overriding special __str__ function to help print key attributes of the instance
        :return: string of key attributes of instance
        """
        return f"name: {self.name}, col: {self.col}, start_x: {self.start_pos_x}, start_y: {self.start_pos_y}"

