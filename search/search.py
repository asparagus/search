#!/usr/bin/python
"""Algorithms for search."""
import abc
import time
from typing import List, Optional
from search import problem


class TimeoutError(Exception):
    """Exception raised when a function call times out."""
    pass


class Search(abc.ABC):

    def __init__(self, problem: problem.Problem):
        self.problem = problem

    @classmethod
    def timecheck(cls, start: float, timeout: float):
        current = time.time()
        if current - start > timeout:
            raise TimeoutError()

    def branch(self, state: problem.State) -> List[problem.State]:
        """Branch a state into its possible continuations."""
        actions = self.problem.actions(state)
        return [action(state) for action in actions]

    def solve(
            self,
            initial_state: Optional[problem.State] = None,
            timeout: Optional[float] = float('inf')) -> Optional[problem.State]:
        """Get a solution to the problem."""
        raise NotImplementedError()
