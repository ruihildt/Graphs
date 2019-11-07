"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # create an empty dict for verts
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # create an empty set
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an error
            raise IndexError("One or more vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store te visited vertices
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # check if that vertex has not been visited
            if v not in visited:
                # mark it as visited
                print('bft', v)
                visited.add(v)
                # add all of its neighbours to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # create a set to store te visited vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # check if that vertex has not been visited
            if v not in visited:
                # mark it as visited
                print('dft', v)
                visited.add(v)
                # add all of its neighbours to the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Add current vert to visited and print it
        visited.add(starting_vertex)
        print("dft_rec", starting_vertex)
        # Recursiion of all the verts in the dict that haven't been visited yet
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store te visited vertices
        visited = list()
        # while queue is not empty
        while q.size() > 0:
            # dequeue to the path
            path = q.dequeue()
            # set a vert to the last item in the path
            vert = path[-1]
            # check if that vertex has not been visited
            if vert not in visited:
                # if vert is equal to the target value
                if vert is destination_vertex:
                    return path
                # mark it as visited
                visited.append(vert)
                # add all of its neighbours to the back of the queue
                for next_vertex in self.vertices[vert]:
                    # set a new path equal to a new list of the a path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vertex)
                    # enqueue the new path
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and enqueue the starting vertex
        s = Stack()
        s.push([starting_vertex])
        # create a set to store te visited vertices
        visited = list()
        # while stack is not empty
        while s.size() > 0:
            # pop to the path
            path = s.pop()
            # set a vert to the last item in the path
            vert = path[-1]
            # check if that vertex has not been visited
            if vert not in visited:
                # if vert is equal to the target value
                if vert is destination_vertex:
                    return path
                # mark it as visited
                visited.append(vert)
                # add all of its neighbours to the back of the stack
                for next_vertex in self.vertices[vert]:
                    # set a new path equal to a new list of the a path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vertex)
                    # enqueue the new path
                    s.push(new_path)
        return None





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
