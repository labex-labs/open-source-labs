# Hanoi

## Problem

Your task is to implement the Towers of Hanoi with 3 towers and N disks. The goal is to move all the disks from the first tower to the third tower, obeying the following simple rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

## Requirements

To solve this problem, you need to meet the following requirements:

- You should have a stack class that can be used for this problem.
- You should validate the inputs before processing them.
- You should ensure that the program fits memory.

## Example Usage

Here are some examples of how the program should behave:

- If there are no towers, an exception should be raised.
- If there are 0 disks, the program should return None.
- If there is only 1 disk, the program should move it from the first tower to the third tower.
- If there are 2 or more disks, the program should move them from the first tower to the third tower, obeying the rules mentioned above.
