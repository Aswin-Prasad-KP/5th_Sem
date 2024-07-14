from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def addEdge(self, s, d):
        self.g[s].append(d)
        self.g[d].append(s)

    def DFS_Util(self, s, vis):
        vis.add(s)
        print(s, end=" ")
        for i in self.g[s]:
            if i not in vis:
                self.DFS_Util(i, vis)

    def DFS(self, s):
        vis = set()
        self.DFS_Util(s, vis)

if __name__ == '__main__':
    N = int(input("Enter no. of Edges : "))
    G = Graph()
    print("Enter edges (Source Destination) : ")
    for i in range(N):
        s, d = map(int, input().split())
        G.addEdge(s, d)
    G.DFS(int(input("Enter Source to Search (DFS) : ")))