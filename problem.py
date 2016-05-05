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
        """Return the initial state for the problem."""
        return ShortestPathState(self.start, 0)

    def is_solution(self, state):
        """Check whether a given state is a solution to the problem."""
        return state.index == self.end

    def branch(self, state):
        """Get all possible states derived from the given state."""
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
        """Initialize an instance of ShortestPathState."""
        self.index = index
        self.value = value
        self.path = path or [index]

    def __repr__(self):
        """String representation of the state."""
        return "{index: %s, value: %s, path: %s}" % (
            self.index, self.value, self.path)

    def __hash__(self):
        """Get a unique hash for the state."""
        return self.index

