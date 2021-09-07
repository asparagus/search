import pytest
from search.examples import ShortestPathProblem
from search import algorithms


@pytest.fixture
def problem():
    adjacency_matrix = [
        [0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
    ]
    start = 4
    end = 0
    return ShortestPathProblem(adjacency_matrix, start, end)


def test_idfs(problem):
    s = algorithms.IterativeDepthFirstSearch(
        problem,
        evaluation_fn=lambda x: x.value,
    )
    sol = s.solve()
    assert sol.value == 2
    assert sol.path == (4, 1, 0)
