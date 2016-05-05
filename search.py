#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Algorithms for search."""
import collections
import heapq


class Search:
    """A type of search."""

    def create_queue(self):
        """Create a queue for storing the states in the search."""
        raise NotImplementedError()

    def push(self, queue, state):
        """Add a state to the queue."""
        raise NotImplementedError()

    def pop(self, queue):
        """Get the next state from the queue."""
        raise NotImplementedError()

    def solve(self, problem):
        """Get a solution to the problem."""
        initial_state = problem.initial_state()

        queue = self.create_queue()
        seen = set()

        self.push(queue, initial_state)
        seen.add(initial_state)

        while len(queue) > 0:
            state = self.pop(queue)
            # print('Analyzing: ' + str(state))

            if problem.is_solution(state):
                return state

            new_states = problem.branch(state)
            # print new_states
            for state in new_states:
                if state not in seen:
                    self.push(queue, state)
                    seen.add(state)

        return None


class BreadthFirstSearch(Search):
    """A breadth first search."""

    def create_queue(self):
        """Create a FIFO queue for storing the states in the search."""
        return collections.deque()

    def push(self, queue, state):
        """Add a state to the queue."""
        queue.append(state)

    def pop(self, queue):
        """Get the next state from the queue."""
        return queue.popleft()


class DepthFirstSearch(Search):
    """A depth first search."""

    def create_queue(self):
        """Create a LIFO stack for storing the states in the search."""
        return []

    def push(self, queue, state):
        """Add a state to the stack."""
        queue.append(state)

    def pop(self, queue):
        """Get the next state from the stack."""
        return queue.pop()


class AStarSearch(Search):
    """An optiminal search."""

    def __init__(self, heuristic=lambda x: 0):
        """
        Initialize an instance of A* search.

        The instance requires an heuristic function which
        receives a state and outputs an expected delta for the solution.

        The heuristic must be admissible to ensure an optimal solution.

        If no heuristic is provided, the Zero Heuristic is used.
        """
        self.heuristic = heuristic

    def create_queue(self):
        """Create a priority queue for storing the states in the search."""
        return []

    def push(self, queue, state):
        """Add a state to the priority queue."""
        g = state.value
        h = self.heuristic(state)
        f = g + h

        heapq.heappush(queue, (f, state))

    def pop(self, queue):
        """Get the next state from the priority queue."""
        return heapq.heappop(queue)[1]


if __name__ == '__main__':
    import problem
    adjacency_matrix = [
        [0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0]]

    start = 4
    end = 0

    spp = problem.ShortestPathProblem(adjacency_matrix, start, end)
    bfs = BreadthFirstSearch()
    dfs = DepthFirstSearch()
    a = AStarSearch()

    print bfs.solve(spp)
    print dfs.solve(spp)
    print a.solve(spp)

