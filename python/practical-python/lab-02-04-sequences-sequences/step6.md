# break statement

You can use the `break` statement to break out of a loop early.

```python
for name in namelist:
    if name == 'Jake':
        break
    ...
    ...
statements
```

When the `break` statement executes, it exits the loop and moves on the next `statements`. The `break` statement only applies to the inner-most loop. If this loop is within another loop, it will not break the outer loop.
