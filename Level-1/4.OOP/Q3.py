class Box:
    def add(self):
        NotImplementedError()

    def empty(self):
        NotImplementedError()

    def count(self):
        NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self.item = []

    def add(self, *items):
        self.item.append(items)

    def empty(self):
        items = self.item
        self.item = []
        return items

    def count(self):
        return len(self.item)


class DictBox(Box):
    def __init__(self):
        self.items = {}

    def add(self, item):
        self.items.update({item: item})

    def empty(self):
        items = list(self.items.values())
        self.items = {}
        return items

    def count(self):
        return len(self.items)


def repack_boxes(*args):
    items, counter, result = [], 0, []
    for boxes in args:
        counter += boxes.count()
        items.append(boxes.empty())

    for list in items:
        for item in list:
            result.append(item)

    while (True):
        for box in args:
            if counter == 0:
                return args
            box.add(result.pop())
            counter -= 1


box1 = ListBox()
for i in range(20):
    box1.add(Item('B1, ' + str(i), i))
print("Box 1: ", box1.count())

box2 = ListBox()
for i in range(9):
    box2.add(Item('B2, ' + str(i), i))
print("Box 2: ", box2.count())

box3 = DictBox()
for i in range(5):
    box3.add(Item('B3, ' + str(i), i))
print("Box 3: ", box3.count())

repack_boxes(box1, box2, box3)

print("Box 1 Counter", box1.count())
print("Box 2 Counter", box2.count())
print("Box 3 Counter", box3.count())
