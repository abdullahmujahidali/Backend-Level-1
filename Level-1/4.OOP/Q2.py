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
        self.item = {}

    def add(self, item):
        self.item.update({item: item})

    def empty(self):
        items = list(self.item.values())
        self.item = {}
        return items

    def count(self):
        return len(self.item)
