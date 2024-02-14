class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("Length of recording cannot be negative")
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Length of recording cannot be negative")
        self.__length = value

# Test the Recording class
if __name__ == "__main__":
    try:
        the_wall = Recording(43)
        print(the_wall.length)
        the_wall.length = 44
        print(the_wall.length)
    except ValueError as e:
        print(e)

