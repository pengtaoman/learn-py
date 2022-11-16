"""
"Properties" section example of writing properties using
`property` decorator

"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        print("########## 初始化")
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        """rectangle height measured from top"""
        print("########### width 被调用")
        return self.x2 - self.x1

    @width.setter
    def width(self, value):
        print("########### width setter 被调用")
        self.x2 = self.x1 + value

    @property
    def height(self):
        """rectangle height measured from top"""
        return self.y2 - self.y1

    @height.setter
    def height(self, value):
        self.y2 = self.y1 + value

    def __repr__(self):
        return "{}({}, {}, {}, {})".format(
            self.__class__.__name__,
            self.x1, self.y1, self.x2, self.y2
        )


class RectangleOld:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def _width_get(self):
        print('########### _width_get 被调用')
        return self.x2 - self.x1

    def _width_set(self, value):
        print('########### _width_set 被调用')
        self.x2 = self.x1 + value

    def _height_get(self):
        return self.y2 - self.y1

    def _height_set(self, value):
        self.y2 = self.y1 + value

    width = property(
        _width_get, _width_set,
        doc="rectangle width measured from left"
    )
    height = property(
        _height_get, _height_set,
        doc="rectangle height measured from top"
    )

    def __repr__(self):
        return "{}({}, {}, {}, {})".format(
            self.__class__.__name__,
            self.x1, self.y1, self.x2, self.y2
        )


class MetricRectangle(Rectangle):
    @property
    def width(self):
        print("----- MetricRectangle -----")
        return "{} meters".format(self.x2 - self.x1)

    @width.setter
    def width(self, value):
        print("########### width setter11111 被调用")
        self.x2 = self.x1 + value


if __name__ == "__main__":
    print("#" * 50)
    rectangleOld = RectangleOld(10, 10, 25, 34)
    print("########初始化后，_width_set被调用了么？ ----没有 _width_get被调用了么？----没有")
    print(rectangleOld.width, rectangleOld.height)
    print(repr(rectangleOld))
    rectangleOld.width = 5000
    print("########  rectangleOld.width = 5000后，_width_set被调用了")
    print(rectangleOld.width, rectangleOld.height)
    print(repr(rectangleOld))
    print("########  居然能通过 width=x2-x1 自动反推 出来 x2=5010")

    mr = MetricRectangle(0, 0, 100, 100)
    print(mr.width)
    mr.width = 8000
    print(mr.width)
    print(mr.width)


    print("#" * 50)
    rectangle = Rectangle(0, 0, 10, 10)
    print(rectangle.width)
    # rectangle.width(200)
    # print(
    #     "At start we have {} with size of {} x {}"
    #     "".format(rectangle, rectangle.width, rectangle.height)
    # )
    #
    # rectangle.width = 2
    # rectangle.height = 8
    # print(
    #     "After resizing we have {} with size of {} x {}"
    #     "".format(rectangle, rectangle.width, rectangle.height)
    # )
