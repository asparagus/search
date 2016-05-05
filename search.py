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
            if problem.is_solution(state):
                return state

            new_states = problem.branch(state)
            for state in new_states:
                if state not in seen:
                    self.push(queue, state)
                    seen.add(state)

        return None


class BreadthFirstSearch(Search):
    """
    A breadth first search.

    >>> bfs = BreadthFirstSearch()
    >>> q = bfs.create_queue()
    >>> bfs.push(q, 1)
    >>> bfs.push(q, 2)
    >>> len(q)
    2
    >>> bfs.pop(q)
    1
    >>> len(q)
    1
    """

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
    """
    A depth first search.

    >>> dfs = DepthFirstSearch()
    >>> q = dfs.create_queue()
    >>> dfs.push(q, 1)
    >>> dfs.push(q, 2)
    >>> len(q)
    2
    >>> dfs.pop(q)
    2
    >>> len(q)
    1
    """

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

        >>> a = AStarSearch()
        >>> a.heuristic(1)
        0
        >>> a.heuristic("Sample")
        0
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


def unit_test():
    """Test the module."""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    unit_test()
