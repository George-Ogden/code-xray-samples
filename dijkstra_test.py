from dijkstra import Edge, dijkstra


def test_dijkstra():
    G = [
        [Edge(1, 6), Edge(3, 7)],
        [Edge(2, 5), Edge(3, 8), Edge(4, -4)],
        [Edge(1, -2), Edge(4, 7)],
        [Edge(2, -3), Edge(4, 9)],
        [Edge(0, 2)],
    ]

    expected_paths = [None, 0, 3, 0, 1]
    expected_weights = [0, 6, 4, 7, 2]

    paths, weights = dijkstra(G, 0)

    assert paths == expected_paths, f"Expected paths: {expected_paths}, but got: {paths}"
    assert weights == expected_weights, f"Expected weights: {expected_weights}, but got: {weights}"
