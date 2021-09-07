from search import heuristic


def test_zero_heuristic():
    h = heuristic.ZeroHeuristic()
    assert h(1) == 0
    assert h("state") == 0
