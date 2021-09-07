"""Classes needed to model a search algorithm."""
import abc


class Action(abc.ABC):
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


class State(abc.ABC):
    """State in the search for a solution."""

    @abc.abstractmethod
    def __hash__(self):
        """Get a unique hash for the state."""
        raise NotImplementedError()

    @abc.abstractmethod
    def __eq__(self, other):
        raise NotImplementedError()

    def __ne__(self, other):
        """Check whether the other object is not equal."""
        return not self.__eq__(other)


class Problem(abc.ABC):
    """A problem to be solved."""

    @abc.abstractmethod
    def initial_state(self):
        """Return the initial state for the problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def is_solution(self, state: State):
        """Check whether a given state is a solution to the problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def actions(self, state: State):
        """Get all possible actions to be executed on a given state."""
        raise NotImplementedError()
