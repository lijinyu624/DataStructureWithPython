from pythonds.graphs import Graph, Vertex

def knightTour(n,path,u,limit):
    # n: the current depth in the search tree
    # path: a list of vertices visited up to this point
    # u: the vertex we wish to explore
    # limit: the number of node in the path
    u.setColor('gray')
    path.append(u)
    if n<limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor()=='white':
                done = knightTour(n+1,path,nbrList[i],limit) # recursively continue to explore one level deeper
            i = i+1
        if not done: # prepare to backtrack if all neighbors have been explored and not yet reach the goal
            path.pop()
            u.setColor('white')
        else:
            done = True # found a successful tour
        return done

# speed-up version
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x:x[0]) # ensure that we select the vertex to go next has the fewest moves
    return [y[1] for y in resList]

