#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Testing BFS, DFS and A* on a ShortestPathProblem.

>>> import problem
>>> import search
>>> adjacency_matrix = [
...     [0, 1, 0, 0, 1],
...     [1, 0, 0, 0, 1],
...     [1, 0, 0, 0, 0],
...     [0, 0, 1, 0, 0],
...     [0, 1, 0, 1, 0]]

>>> start = 4
>>> end = 0

>>> spp = problem.ShortestPathProblem(adjacency_matrix, start, end)
>>> bfs = search.BreadthFirstSearch()
>>> dfs = search.DepthFirstSearch()
>>> a = search.AStarSearch()

>>> bfs.solve(spp)
{index: 0, value: 2, path: [4, 1, 0]}

>>> dfs.solve(spp)
{index: 0, value: 3, path: [4, 3, 2, 0]}

>>> a.solve(spp)
{index: 0, value: 2, path: [4, 1, 0]}

"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
