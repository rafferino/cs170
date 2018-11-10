import names
import numpy as np
import numpy.random as random
import classroom as c
import networkx as nx
import pylab as plt

def main():
    C = c.Classroom(25, 5, 5)
    C.saveGraphtoFile('test')
    G = nx.read_gml('test.gml', 'label')




if __name__ == "__main__":
    main()



# G = nx.Graph()
# for i in range(5):
#     length = len(C.classroom)
#     i, j = random.randint(length), random.randint(length)
#     print(C.classroom[i], C.classroom[j])
#     G.add_edge(C.classroom[i], C.classroom[j])
# nx.draw_networkx(G, with_labels = True)
# plt.savefig('classroom.png')
