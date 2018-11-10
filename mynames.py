import numpy.random as random

class MyNames:

    def __init__(self):
        self.names = self.readNames('names.txt')
        self.size = len(self.names)

    def readNames(self, filename):
        fp = open(filename, 'r')
        names = []
        name = fp.readline()
        while (name):
            names.append(name.rstrip('\n'))
            name = fp.readline()
        return names

    def getName(self):
        return self.names[random.randint(0, self.size)]
