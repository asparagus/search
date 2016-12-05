#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Classes needed to model a search algorithm."""
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Problem:
    """A problem to be solved."""

    @abc.abstractmethod
    def initial_state(self):
        """Return the initial state for the problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def is_solution(self, state):
        """Check whether a given state is a solution to the problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def actions(self, state):
        """Get all possible actions to be executed on a given state."""
        raise NotImplementedError()


@six.add_metaclass(abc.ABCMeta)
class Action:
    """An action for a given problem."""

    @abc.abstractmethod
    def __call__(self, state):
        """Execute the action on a state."""
        raise NotImplementedError()

    def __str__(self):
        """The string representation of this action."""
        return self.__class__.__name__

    def __repr__(self):
        """The string representation of this action."""
        return str(self)


@six.add_metaclass(abc.ABCMeta)
class State:
    """(Intermediate) State in the search for a solution."""

    @abc.abstractmethod
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

    def actions(self, state):
        """Get all possible actions from the given state."""
        index = state.index
        valid_actions = [
            ShortestPathNodeTraversal(index, other)
            for other, valid in enumerate(self.adjacency_matrix[index])
            if valid
        ]

        return valid_actions


class ShortestPathNodeTraversal(Action):
    """Node Traversal action for the ShortestPath Problem."""

    def __init__(self, start, end):
        """Initialize the node traversal action."""
        self.start = start
        self.end = end

    def __call__(self, state):
        """Execute the node traversal on a given state."""
        return ShortestPathState(
            self.end,
            state.value + 1,
            state.path + [self.end]
        )


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