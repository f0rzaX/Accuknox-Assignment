class Rectangle:
    """
    Initialization (__init__ method):
    The __init__ method takes length and width as integer arguments and assigns them to instance variables.
    """
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    """
    Iteration (__iter__ method):
    The __iter__ method makes the Rectangle instance iterable.
    """
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Creating an instance of Rectangle
rectangle = Rectangle(5, 10)

# Iterating over the instance
for dimension in rectangle:
    print(dimension)
    # {'length': 5}
    # {'width': 10}
