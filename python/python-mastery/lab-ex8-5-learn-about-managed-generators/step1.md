# Generators as tasks

If a file `multitask.py`, define the following code:

```python
# multitask.py

from collections import deque

tasks = deque()
def run():
    while tasks:
        task = tasks.popleft()
        try:
            task.send(None)
            tasks.append(task)
        except StopIteration:
            print('Task done')
```

This code implements a tiny task scheduler that runs generator functions.
Try it by running it on the following functions.

```python
# multitask.py
...

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1

def countup(n):
    x = 0
    while x < n:
        print('Up we go', x)
        yield
        x += 1

if __name__ == '__main__':
    tasks.append(countdown(10))
    tasks.append(countdown(5))
    tasks.append(countup(20))
    run()
```

When you run this, you should see output from all of the generators
interleaved together. For example:

```python
T-minus 10
T-minus 5
Up we go 0
T-minus 9
T-minus 4
Up we go 1
T-minus 8
T-minus 3
Up we go 2
T-minus 7
T-minus 2
Up we go 3
T-minus 6
T-minus 1
Up we go 4
T-minus 5
Task done
Up we go 5
T-minus 4
Up we go 6
T-minus 3
Up we go 7
T-minus 2
Up we go 8
T-minus 1
Up we go 9
Task done
Up we go 10
Up we go 11
Up we go 12
Up we go 13
Up we go 14
Up we go 15
Up we go 16
Up we go 17
Up we go 18
Up we go 19
Task done
```

That's interesting, but not especially compelling. Move on to the next example.
