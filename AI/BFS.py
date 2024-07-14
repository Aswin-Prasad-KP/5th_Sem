from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def addEdge(self, s, d):
        self.g[s].append(d)
        self.g[d].append(s)

    def BFS(self, s):
        vis = [False] * (max(self.g) + 1)
        q = []
        q.append(s)
        vis[s] = True
        while q:
            s = q.pop(0)
            print(s, end=" ")
            for i in self.g[s]:
                if not vis[i]:
                    q.append(i)
                    vis[i] = True

if __name__ == '__main__':
    N = int(input("Enter no. of Edges : "))
    G = Graph()
    print("Enter edges (Source Destination) : ")
    for i in range(N):
        s, d = map(int, input().split())
        G.addEdge(s, d)
    G.BFS(int(input("Enter Source to Search (BFS) : ")))