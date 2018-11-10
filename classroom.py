import mynames
import numpy as np
import numpy.random as random
import networkx as nx
import pylab as plt

class Classroom:


    def __init__(self, size, numgroups, groupsize):
        self.n = mynames.MyNames()
        self.classroom = self.generateClass(size)
        self.size = len(self.classroom)
        self.rowdies = self.generateRowdies(numgroups, groupsize)
        self.friendGraph = self.generateGraph()

    def generateClass(self, size):
        classroom = []
        for i in range(size):
            name = self.n.getName()
            while name in classroom:
                name = self.n.getName()
            classroom.append(name)
        return classroom

    def generateRowdies(self, numgroups, groupsize):
        rowdies = []
        checkGroup = set()
        for i in range(numgroups):
            checkName = set()
            group = []
            for j in range(random.randint(max(2, groupsize//2), groupsize)):
                idx = random.randint(self.size)
                while (idx in checkName):
                    idx = random.randint(self.size)
                checkName.add(idx)
                group.append(self.classroom[idx])
            rowdies.append(group)
        return rowdies

    def generateGraph(self, prob=0.9):
        G = nx.Graph()
        for student in self.classroom:
            G.add_node(student)
            for other in self.classroom:
                p = random.random(1)
                if p > prob and other != student:
                    G.add_edge(student,other)
        return G

    def displayFriendGraph(self, block=True, save=False, filename=''):
        plt.figure()
        nx.draw_networkx(self.friendGraph, with_labels = True)
        plt.show(block=block)
        if save:
            plt.savefig(filename+'.png')


    def printRowdies(self):
        for rowdy in self.rowdies:
            print(rowdy)
        return

    def saveGraphtoFile(self, filename):
        nx.write_gml(self.friendGraph, filename+'.gml')
