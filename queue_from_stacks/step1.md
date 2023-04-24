# Queue From Stacks

## Problem

Implementing a queue using two stacks can be a challenging problem. The basic idea is to use one stack for enqueue operations and the other stack for dequeue operations. When an element is enqueued, it is pushed onto the first stack. When an element is dequeued, it is popped from the second stack. If the second stack is empty, we pop all the elements from the first stack and push them onto the second stack in reverse order. This ensures that the first element that was enqueued is the first element that is dequeued.

## Requirements

To solve this problem, we need to consider the following requirements:

- We need to implement two methods: enqueue and dequeue.
- We need to assume that we already have a stack class that can be used for this problem.
- We cannot push a None value to the Stack.
- We can assume that this problem fits memory.

## Example Usage

Here are some examples of how we can use our implementation of a queue using two stacks:

- Enqueue and dequeue on an empty stack: We can enqueue an element onto the queue and then dequeue it to ensure that the queue is working correctly.
- Enqueue and dequeue on a non-empty stack: We can enqueue multiple elements onto the queue and then dequeue them to ensure that the queue is working correctly.
- Multiple enqueue in a row: We can enqueue multiple elements onto the queue in a row and then dequeue them to ensure that the queue is working correctly.
- Multiple dequeue in a row: We can enqueue multiple elements onto the queue and then dequeue them in a row to ensure that the queue is working correctly.
- Enqueue after a dequeue: We can enqueue an element onto the queue, dequeue it, and then enqueue another element onto the queue to ensure that the queue is working correctly.
- Dequeue after an enqueue: We can enqueue an element onto the queue, dequeue it, and then enqueue another element onto the queue to ensure that the queue is working correctly.
