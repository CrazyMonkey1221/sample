def astar(start_node,stop_node):
    
    open_set = set(start_node)
    closed_set = set()

    g = {}
    parent = {}

    g[start_node] = 0
    parent[start_node] = start_node

    while len(open_set) > 0 :
        n = None

        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
            
        if n == stop_node or grap_node[n]==None:
            pass
        else:
            for (m,weight) in get_neighbors(n):
                if m not in open_set or m not in closed_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m]>g[n]+weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        
        if n == None:
            print("No path")
            return None
        
        if n == stop_node:
            p = []
            while parent[n]!=n:
                p.append(n)
                n = parent[n]

            p.append(start_node)
            p.reverse()
            print('Path found {}'.format(p))
            return p

        open_set.remove(n)
        closed_set.add(n)
    
    print('no path')
    return None

def get_neighbors(v):
    if v in grap_node:
        return grap_node[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A':10,
        'B':8,
        'C':5,
        'D':7,
        'E':3,
        'F':6,
        'G':5,
        'H':3,
        'I':1,
        'J':0
    }
    return H_dist[n]

grap_node = {
    
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],

}

astar('A','J')