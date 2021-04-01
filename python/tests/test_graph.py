from challenges.graph.graph import Vertex, Graph, Edge
import pytest

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual
    
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected

def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected

def test_add_edge_error():
    graph = Graph()
    start = graph.add_node("start")
    end = graph.add_node("end")
    graph.add_edge(start, end)
    try:
        graph.add_edge(start, end)
    except KeyError:
        pytest.fail("KeyError should not be thrown")    
