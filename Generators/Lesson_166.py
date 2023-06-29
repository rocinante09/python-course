class MyGenerator():
    current=0
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


    def __iter__(self):
        return self;

    def __next__(self):
        if MyGenerator.current < self.stop:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration


gen = MyGenerator(0,100)
for i in gen:
    print(i)

