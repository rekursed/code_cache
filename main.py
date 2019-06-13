from graph.bfs import breadth_first_search
if __name__ == '__main__':
    print('abc')
    graph = {0: [1, 2], 1: [2], 2: []}
    breadth_first_search(graph, 0)
