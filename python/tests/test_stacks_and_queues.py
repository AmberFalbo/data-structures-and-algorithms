import pytest
from challenges.stacks_and_queues.stacks_and_queues import Node, Stack, InvalidOperationError, Queue

def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    actual = s.pop()
    expected = "banana"
    assert actual == expected


def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert expected == actual
    
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()
    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()
    assert str(e.value) == "Method not allowed on empty collection"

# *******Testing Queue********

def test_enqueue_one_node():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected

def test_enqueue_add_multiple_nodes():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("pear")
    q.enqueue("peach")
    actual = q.counter
    expected = 4
    assert actual == expected

def test_dequeue_one_node():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("pear")
    q.enqueue("peach")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected
    
def test_dequeue_entire_queue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("pear")
    q.enqueue("peach")
    while q.counter > 0:
        q.dequeue()
    actual = q.counter
    expected = 0
    assert actual == expected

def test_peek_expected_error():
    q = Queue()
    with pytest.raises(InvalidOperationError) as e:
        q.peek()
    assert str(e.value) == "Method not allowed on empty collection"

def test_peek_actual_value():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.peek()
    expected = "apple"
    assert actual == expected