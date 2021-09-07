import pytest
from search import algorithms
from search.examples import ShortestPathProblem


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


def test_bfs(problem):
    bfs = algorithms.BreadthFirstSearch(problem)
    sol = bfs.solve()
    assert sol.value == 2
    assert sol.path == (4, 1, 0)


def test_dfs(problem):
    dfs = algorithms.DepthFirstSearch(problem)
    sol = dfs.solve()
    assert sol.value == 2
    assert sol.path == (4, 1, 0)


def test_a_star(problem):
    a = algorithms.BestFirstSearch(problem, evaluation_fn=lambda x: x.value)
    sol = a.solve()
    assert sol.value == 2
    assert sol.path == (4, 1, 0)


def test_beam_search(problem):
    beam = algorithms.BeamSearch(problem, evaluation_fn=lambda x: x.value)
    sol = beam.solve()
    assert sol.value == 2
    assert sol.path == (4, 1, 0)
