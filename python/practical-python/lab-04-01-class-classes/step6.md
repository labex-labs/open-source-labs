# Class Scoping

Classes do not define a scope of names.

```python
class Player:
    ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NO. Calls a global `move` function
        self.move(-amt, 0)  # YES. Calls method `move` from above.
```

If you want to operate on an instance, you always refer to it explicitly (e.g., `self`).

Starting with this set of exercises, we start to make a series of
changes to existing code from previous sections. It is critical that
you have a working version of Exercise 3.18 to start. If you don't
have that, please work from the solution code found in the
`Solutions/3_18` directory. It's fine to copy it.
