#!/usr/bin/python3
"""define square class"""


class Square():
    """square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """square constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """square area"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """square perimeter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """represent square as str"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """create square object"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())