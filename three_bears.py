

class ThreeBears:
    def __init__(self):
        self.count = 0
    def __iter__(self):
        return self
    def next(self):
        if self.count==0:
            self.count = self.count + 1
            return "mom"
        elif self.count==1:
            self.count = self.count + 1
            return "dad"
        elif self.count==2:
            self.count = self.count + 1
            return "baby"
        else:
            raise StopIteration()

# odd way to call this
b = ThreeBears()
it = iter(b)
print it.next()
print it.next()
print it.next()
# print it.next()

# better way to call it

for b in ThreeBears():
    print b
