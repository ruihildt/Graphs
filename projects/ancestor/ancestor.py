from util import Queue  # These may come in handy

def earliest_ancestor(ancestors, starting_vertex):
    pass

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# Print the list to a dictionary and reverse it
# now parents are children and we can use our usual BFS algo to search for longer paths
def reverse_ancestors(ancestors):
    # print list to a dict
    ancestors_dict = dict(ancestors)
    # invert
    reversed_ancestors = {} 
    for key, value in ancestors_dict.items(): 
        if value in reversed_ancestors: 
            reversed_ancestors[value].append(key) 
        else: 
            reversed_ancestors[value]=[key]
    return reversed_ancestors
# print(reverse_ancestors(test_ancestors))


# Print all the path to a list using BFS
def bfs(ancestors, starting_vertex, next_vertex=None):
    # reverse the ancestors
    reverted_ancestors = reverse_ancestors(ancestors)
    #create empty list with possible path
    paths = list()
    # create an empty queue and enqueue the starting vertex
    q = Queue()
    q.enqueue([starting_vertex])
    # create a set to store the visited vertices
    visited = list()
    # while queue is not empty
    while q.size() > 0:
        # dequeue to the path
        path = q.dequeue()
        print('path', path)
        # set a vert to the last item in the path
        vert = path[-1]
        print('vert', vert)
        # check if that vertex has not been visited
        if vert not in visited:
            # mark it as visited
            visited.append(vert)
            # add all of its neighbours to the back of the queue
            for next_vertex in reverted_ancestors[vert]:
                # set a new path equal to a new list of the a path
                new_path = list(path)
                # append next vert to new path
                new_path.append(next_vertex)
                # enqueue the new path
                q.enqueue(new_path)

    return None

print(bfs(test_ancestors, 6))

# compare and keep only the longest(s) one(s)
# and return the path with the smallest latest value from the list