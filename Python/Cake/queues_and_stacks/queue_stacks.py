# https://www.interviewcake.com/question/python/queue-two-stacks?course=fc1&section=queues-stacks
# Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and
# a dequeue method and it should be "first in first out" (FIFO).
#
# Optimize for the time cost of mm calls on your queue. These can be any mix of enqueue and dequeue calls.
#
# Assume you already have a stack implementation and it gives O(1)O(1) time push and pop.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class QueueStack:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, item):
        self.enqueue_stack.push(item)

    def dequeue(self):
        if not self.dequeue_stack.items:
            if not self.enqueue_stack.items:
                rraise Exception
            while self.enqueue_stack.items:
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()


queue_stack = QueueStack()
queue_stack.enqueue(0)
queue_stack.enqueue(1)
queue_stack.enqueue(2)
print(queue_stack.dequeue())
print(queue_stack.dequeue())
print(queue_stack.dequeue())
queue_stack.enqueue(8)
queue_stack.enqueue(9)
queue_stack.enqueue(10)
print(queue_stack.dequeue())
print(queue_stack.dequeue())
print(queue_stack.dequeue())

# Tests
import unittest
class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)