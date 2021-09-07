"""Contains the base class for transformating one problem to another."""
import abc
from typing import Any


class Transformation(abc.ABC):
    """Base class for a transformation."""

    @abc.abstractmethod
    def apply(self, problem: Any):
        """Applythe transformation on a problem."""
        raise NotImplementedError()

    @abc.abstractmethod
    def revert(self, solution: Any):
        """Revert the transformation on the problem's output."""
        raise NotImplementedError()
