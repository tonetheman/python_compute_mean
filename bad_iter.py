

class BadObject:
    def __iter__(self):
        return self
    def next(self):
        return 0

bo = BadObject()

it = iter(bo)
print it.next()
