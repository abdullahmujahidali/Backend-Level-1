class Box:
    def add(self):
        pass

    def empty(self):
        pass

    def count(self):
        pass


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)


box1 = ListBox()
box2 = DictBox()

box1.add(Item(str(i), i) for i in range(20))
print(box1.count())
