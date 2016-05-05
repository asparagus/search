#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Classes needed to model a search algorithm."""


class Problem:
    """A problem to be solved."""

    def initial_state(self):
        """Return the initial state for the problem."""
        raise NotImplementedError()

    def is_solution(self, state):
        """Check whether a given state is a solution to the problem."""
        raise NotImplementedError()

    def branch(self, state):
        """Get all possible states derived from the given state."""
        raise NotImplementedError()


class State:
    """(Intermediate) State in the search for a solution."""

    def __hash__(self):
        """Get a unique hash for the state."""
        raise NotImplementedError()

    def __eq__(self, other):
        """Check whether the other object is equal."""
        if isinstance(other, self.__class__):
            return hash(self) == hash(other)
        else:
            return False

    def __ne__(self, other):
        """Check whether the other object is not equal."""
        return not self.__eq__(other)


class ShortestPathProblem(Problem):
    """Basic shortest path problem."""

    def __init__(self, adjacency_matrix, node_start, node_end):
        """Initialize an instance of ShortestPathProblem."""
        self.adjacency_matrix = adjacency_matrix
        self.start = node_start
        self.end = node_end

    def initial_state(self):
        """
        Return the initial state for the problem.

        >>> spp = ShortestPathProblem([[0,1],[1,0]], 0, 1)
        >>> spp.initial_state()
        {index: 0, value: 0, path: [0]}

        >>> spp = ShortestPathProblem([[0,1],[1,0]], 1, 0)
        >>> spp.initial_state()
        {index: 1, value: 0, path: [1]}
        """
        return ShortestPathState(self.start, 0)

    def is_solution(self, state):
        """
        Check whether a given state is a solution to the problem.

        >>> spp = ShortestPathProblem([[0,1],[1,0]], 0, 1)
        >>> state0 = ShortestPathState(0, 0, [0])
        >>> spp.is_solution(state0)
        False
        >>> state1 = ShortestPathState(1, 0, [0, 1])
        >>> spp.is_solution(state1)
        True
        """
        return state.index == self.end

    def branch(self, state):
        """
        Get all possible states derived from the given state.

        >>> spp = ShortestPathProblem([[0,1, 1],[1,0,1], [1,1,0]], 0, 2)
        >>> state = spp.initial_state()
        >>> next = spp.branch(state)
        >>> len(next)
        2
        >>> next[0]
        {index: 1, value: 1, path: [0, 1]}
        >>> next[1]
        {index: 2, value: 1, path: [0, 2]}
        """
        index = state.index
        value = state.value
        path = state.path
        branches = [
            ShortestPathState(i, value + 1, path + [i])
            for i, valid in enumerate(self.adjacency_matrix[index])
            if valid]

        return branches


class ShortestPathState(State):
    """(Intermediate) State in the search for a solution."""

    def __init__(self, index, value, path=None):
        """
        Initialize an instance of ShortestPathState.

        >>> s = ShortestPathState(1, 2)
        >>> s.index
        1
        >>> s.value
        2
        >>> s.path
        [1]
        """
        self.index = index
        self.value = value
        self.path = path or [index]

    def __repr__(self):
        """
        String representation of the state.

        >>> s = ShortestPathState(1, 2)
        >>> print s
        {index: 1, value: 2, path: [1]}
        >>> print [s]
        [{index: 1, value: 2, path: [1]}]
        """
        return "{index: %s, value: %s, path: %s}" % (
            self.index, self.value, self.path)

    def __hash__(self):
        """
        Get a unique hash for the state.

        >>> s1 = ShortestPathState(1, 2)
        >>> hash(s1)
        1
        >>> s2 = ShortestPathState(1, 3)
        >>> hash(s2)
        1
        >>> s = set([s1])
        >>> s2 in s
        True
        """
        return self.index


def unit_test():
    """Test the module."""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    unit_test()
