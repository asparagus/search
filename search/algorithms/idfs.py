import depq
import time
from typing import Callable, Optional
from search import algorithms
from search import heuristic
from search import problem


class IterativeDepthFirstSearch(algorithms.BestFirstSearch):
    """
    An optimal iterative search.
    This algorithm iteratively improves the found solution until it's optimal
    or time runs out.
    """

    def __init__(
            self,
            problem: problem.Problem,
            evaluation_fn: Callable[[problem.State], float],
            heuristic_fn: Optional[heuristic.Heuristic] = heuristic.ZeroHeuristic(),
        ):
        super().__init__(problem, evaluation_fn, heuristic_fn=heuristic_fn)

    def solve(
            self,
            initial_state: Optional[problem.State] = None,
            timeout: Optional[float] = float('inf'),
            soft_timeout: Optional[float] = float('inf'),
        ) -> Optional[problem.State]:
        """Get a solution to the problem."""
        soft_timeout = min(timeout, soft_timeout)
        start = time.time()
        seen = set()
        state = initial_state or self.problem.initial_state()
        priority_queue = depq.DEPQ()
        self.push(priority_queue, state)

        best_solution = None
        best_value = float('inf')
        try:
            while priority_queue:
                self.timecheck(start, timeout)
                if best_solution:
                    self.timecheck(start, soft_timeout)
                state, value = priority_queue.poplast()
                if value >= best_value:  # Hope is lost
                    break

                remaining_time = timeout - (time.time() - start)
                new_solution = self.run(
                    state, priority_queue, seen, remaining_time)

                if new_solution:
                    new_value = self.evaluate(new_solution)
                    if best_solution is None or new_value < best_value:
                        best_solution = new_solution
                        best_value = new_value
        except TimeoutError:
            if not best_solution:
                raise
        return best_solution

    def run(self,
            initial_state: problem.State,
            priority_queue: depq.DEPQ,
            seen: set,
            timeout: Optional[float] = float('inf'),
        ) -> Optional[problem.State]:
        """
        Get a temporary solution.
        Multiple calls to run function will improve on the initial solution.
        """
        start = time.time()
        current_state = initial_state
        while True:
            self.timecheck(start, timeout)
            if self.problem.is_solution(current_state):
                return current_state

            branched_states = self.branch(current_state)
            new_states = [
                state for state in branched_states
                if state not in seen
            ]

            if new_states:
                # Continue the run through the first state
                current_state = new_states[0]
                seen.add(current_state)
                for state in new_states[1:]:
                    self.push(priority_queue, state)
                    seen.add(state)

            else: # No way to continue this run
                break

        return None
