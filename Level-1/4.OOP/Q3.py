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


def repack_boxes(boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())
    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break


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

repack_boxes([box1, box2, box3])

print(box1.count())
print(box2.count())
print(box3.count())
