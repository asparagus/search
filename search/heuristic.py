"""Heuristic functions to evaluate states."""
import abc
from search import problem


class Heuristic(abc.ABC):
    """An evaluation function used for heuristic purposes."""

    @abc.abstractmethod
    def __call__(self, state: problem.State) -> float:
        """Evaluate a state."""
        raise NotImplementedError()


class ZeroHeuristic(Heuristic):
    """The Zero Heuristic."""

    def __call__(self, state: problem.State) -> float:
        """Evaluate a state, return zero."""
        return 0
