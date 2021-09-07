"""Algorithms for search."""
import collections
import depq
import time
from typing import Callable, List, Optional
from search import heuristic
from search import problem
from search import search


class DepthFirstSearch(search.Search):
    """DepthFirstSearch algorithm."""

    def solve(
            self,
            initial_state: Optional[problem.State] = None,
            timeout: Optional[float] = float('inf'),
        ) -> Optional[problem.State]:
        """
        Solve using DFS.

        Use a stack to store states and pick the top one to expand & continue.
        """
        start = time.time()
        seen = set()
        state = initial_state or self.problem.initial_state()
        stack = [state]
        while stack:
            self.timecheck(start, timeout)
            current = stack.pop()
            children = self.branch(current)
            for state in children:
                if self.problem.is_solution(state):
                    return state
            unseen_children = [c for c in children if c not in seen]
            seen.update(unseen_children)
            stack.extend(unseen_children[::-1])
        return None


class BreadthFirstSearch(search.Search):
    """BreadthFirstSearch algorithm."""

    def solve(
            self,
            initial_state: Optional[problem.State] = None,
            timeout: Optional[float] = float('inf'),
        ) -> Optional[problem.State]:
        """
        Solve using BFS.

        Use a queue to store states and pick the 1st one to expand & continue.
        """
        start = time.time()
        seen = set()
        state = initial_state or self.problem.initial_state()
        queue = collections.deque([state])
        while queue:
            self.timecheck(start, timeout)
            current = queue.popleft()
            children = self.branch(current)
            for state in children:
                if self.problem.is_solution(state):
                    return state
            unseen_children = [c for c in children if c not in seen]
            seen.update(unseen_children)
            queue.extend(unseen_children[::-1])
        return None


class BestFirstSearch(search.Search):
    """
    BestFirstSearch algorithm (a.k.a. A*).

    A* expands the most promising state at each point, according to the
    evaluation and heuristic functions provided.
    """

    def __init__(
            self,
            problem: problem.Problem,
            evaluation_fn: Callable[[problem.State], float],
            heuristic_fn: Optional[heuristic.Heuristic] = heuristic.ZeroHeuristic(),
        ):
        """
        Initialize an instance of A* search.

        The instance requires an heuristic function which
        receives a state and outputs an expected delta for the solution.

        The heuristic must be admissible to ensure an optimal solution.

        If no heuristic is provided, the ZeroHeuristic is used.
        """
        super().__init__(problem)
        self.evaluation_fn = evaluation_fn
        self.heuristic_fn = heuristic_fn or heuristic.ZeroHeuristic()
        self.value_states_dict = {}

    def solve(
            self,
            initial_state: Optional[problem.State] = None,
            timeout: Optional[float] = float('inf'),
        ) -> Optional[problem.State]:
        """
        Solve using Best First Search (A*).

        Prioritize state expansion according to the evaluation + heuristic fns.
        """
        start = time.time()
        seen = set()
        state = initial_state or self.problem.initial_state()
        priority_queue = depq.DEPQ()
        self.push(priority_queue, state)
        while priority_queue:
            self.timecheck(start, timeout)
            current, _ = priority_queue.poplast()
            children = self.branch(current)
            for state in children:
                if self.problem.is_solution(state):
                    return state
            unseen_children = [c for c in children if c not in seen]
            seen.update(unseen_children)
            for child in unseen_children[::-1]:
                self.push(priority_queue, child)
        return None

    def push(self, priority_queue: depq.DEPQ, state: problem.State):
        """Push a state into the priority queue."""
        value = self.evaluate(state)
        priority_queue.insert(state, value)

    def evaluate(self, state: problem.State):
        """Evaluate a state using evaluation and heuristic functions."""
        return self.evaluation_fn(state) + self.heuristic_fn(state)


class BeamSearch(BestFirstSearch):
    """
    BeamSearch algorithm, a modified BestFirstSearch.

    BeamSearch limits the memory used by keeping only a limited number
    of candidate solutions.
    """

    def __init__(
            self,
            problem: problem.Problem,
            evaluation_fn: Callable[[problem.State], float],
            heuristic_fn: Optional[heuristic.Heuristic] = heuristic.ZeroHeuristic(),
            beam_width: int = 100):
        """
        Initialize an instance of BeamSearch.

        The instance requires an heuristic function which
        receives a state and outputs an expected delta for the solution.

        The heuristic must be admissible to ensure an optimal solution.

        If no heuristic is provided, the ZeroHeuristic is used.
        """
        super().__init__(problem, evaluation_fn, heuristic_fn=heuristic_fn)
        self.beam_width = beam_width

    def push(self, priority_queue: depq.DEPQ, state: problem.State):
        """Push a state into the priority queue. Drop excess states."""
        value = self.evaluate(state)
        priority_queue.insert(state, value)
        while len(priority_queue) > self.beam_width:
            priority_queue.popfirst()
