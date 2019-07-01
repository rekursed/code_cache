#!/bin/python3

import heapq
import os
import sys


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, source, target):
        '''
        Dijkstra's algorithm finds the shortest path from source to target
        :param source: Source vertex
        :param target: Destination vertex
        :return:
        '''
        graph = self.graph
        INF = sys.maxsize
        predceesor = {x: x for x in graph}
        distance = {x: INF for x in graph}
        distance[source] = 0
        queue = []
        heapq.heappush(queue, [distance[source], source])

        while (queue):
            # print(queue)
            [u_distance, u_id] = heapq.heappop(queue)
            if u_distance == distance[u_id]:
                if u_id == target:
                    break
                for v in graph[u_id]:
                    [v_id, weight] = v
                    new_dist = distance[u_id] + weight
                    old_dist = distance[v_id]
                    if distance[u_id] + weight < distance[v_id]:
                        distance[v_id] = distance[u_id] + weight
                        heapq.heappush(queue, [distance[v_id], v_id])
                        predceesor[v_id] = u_id
            # print(distance)
        if distance.get(target,INF) == INF:
            return
        else:
            print(f'{distance[target]}')
            return


def main():
    file_name = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    # root_path = os.path.dirname(os.path.realpath(__file__))
    # file_path = os.path.join(root_path, 'files', file_name)
    graph = dict()
    with open(file_name, 'r') as data:
        sys.stdin = data
        nodes = int(input().strip())
        for i in range(nodes):
            node_id = input().strip()
            graph[node_id] = list()
        # print(graph)
        edges = int(input().strip())
        for i in range(edges):
            [start, end, weight] = input().strip().split(' ')
            graph[start].append((end, int(weight)))
            graph[end].append((start, int(weight)))
        # print(graph)
        graph_obj = Graph(graph)

        graph_obj.dijkstra(source, destination)


if __name__ == '__main__':
    main()
