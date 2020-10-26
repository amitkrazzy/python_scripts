2 ways:
'''class firstnum(object):
    def __init__(self,n):
        self.last=n
        self.num=0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()


    def next(self):
        if self.num < self.last:
            cur , self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

print(sum(firstnum(10)))
'''

def gen(n):
    i=0
    while i<n:
        yield i
        i=i+1

print(sum(gen(10)))
