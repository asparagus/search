import pytest
from search import examples


@pytest.fixture
def spp():
    adjacency_matrix = [[0, 1], [1, 0]]
    spp = examples.ShortestPathProblem(adjacency_matrix, start=0, end=1)
    return spp


def test_initial_state(spp):
    expected_initial = examples.Path(value=0, path=(0,))
    assert spp.initial_state() == expected_initial


def test_solution_check(spp):
    expected_solution = examples.Path(value=0, path=(0, 1))
    assert not spp.is_solution(spp.initial_state())
    assert spp.is_solution(expected_solution)
