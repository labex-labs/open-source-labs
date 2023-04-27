# Queue List

## Problem

Implement a queue with enqueue and dequeue methods using a linked list. The enqueue method should add an element to the end of the queue, and the dequeue method should remove an element from the front of the queue. If the queue is empty, dequeue should return None.

## Requirements

To implement the queue, we need to follow the following requirements:

- If there is one item in the list, the first and last pointers should both point to it.
- If there are no items on the list, the first and last pointers should be None.
- If you dequeue on an empty queue, it should return None.
- We can assume that this fits memory.

## Example Usage

### Enqueue

- Enqueue to an empty queue: If the queue is empty, the enqueue method should add the element as the first and last element of the queue.
- Enqueue to a non-empty queue: If the queue is not empty, the enqueue method should add the element to the end of the queue.

### Dequeue

- Dequeue an empty queue -> None: If the queue is empty, the dequeue method should return None.
- Dequeue a queue with one element: If the queue has only one element, the dequeue method should remove the element and set the first and last pointers to None.
- Dequeue a queue with more than one element: If the queue has more than one element, the dequeue method should remove the first element and set the first pointer to the next element.
