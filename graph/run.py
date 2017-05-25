from graph import Graph

g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertList)

G = [
      [0,1,5],[0,5,2],[1,2,4],[2,3,9],
      [3,4,7],[3,5,3],[4,0,1],[5,4,8],
      [5,2,1]
]

for i in G:
    g.addEdge(i[0],i[1],i[2])

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

