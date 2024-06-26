import heapq
graph = {
    'A': [(1,'B'), (5, 'C')],
    'B': [(2,'D')],
    'C': [(10, 'D')]
    }
h = {'A':6, 'B':4, 'C':2, 'D':0}
source = 'A'
dest = 'D'
visited = set()
visql = [(h[source], source, source)]
mincos = 0
fpath = False
path = None

while not fpath:
    x,y,z = heapq.heappop(visql)
    visited.add(y)
    if y == dest:
        mincos = x
        path = z
        fpath = True
        continue
    else:
        for i in graph[y]:
            if i[1] not in visited:
                heapq.heappush(visql,(i[0]+h[i[1]]+x-h[y], i[1], z+i[1]))
            else:
                continue

print(f"Minimum cost from source to destination is {mincos}")
print(f"Path: {'->'.join(list(path))}")
                
