

class SortedSet(set):

    def __init__(self, items):
        items.sort();
        super(type(self), self).__init__(items)
