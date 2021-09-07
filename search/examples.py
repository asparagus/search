"""Example problem."""
import attr
from typing import Tuple
from search import problem


@attr.s
class NodeTraversal(problem.Action):
    """Action for the ShortestPath Problem."""

    start = attr.ib(type=int)
    end = attr.ib(type=int)

    def __call__(self, state):
        """Execute the node traversal on a given state."""
        extended_path = state.path + (self.end,)
        new_state = Path(
            value=len(extended_path) - 1,
            path=extended_path,
        )
        return new_state


@attr.s(frozen=True)
class Path(problem.State):
    """Possible solution to the Shortest Path Problem."""

    value = attr.ib(type=float)
    path = attr.ib(type=Tuple[int])

    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()


class ShortestPathProblem(problem.Problem):
    """Basic shortest path problem."""

    def __init__(self, adjacency_matrix, start: int, end: int):
        """Initialize an instance of ShortestPathProblem."""
        self.adjacency_matrix = adjacency_matrix
        self.start = start
        self.end = end

    def initial_state(self):
        """Return the initial state for the problem."""
        return Path(0, (self.start,))

    def is_solution(self, state: Path):
        """Check whether a given state is a solution to the problem."""
        return state.path and state.path[-1] == self.end

    def actions(self, state: Path):
        """Get all possible actions from the given state."""
        last_index = state.path[-1]
        return [
            NodeTraversal(last_index, other)
            for other, valid in enumerate(self.adjacency_matrix[last_index])
            if valid
        ]
