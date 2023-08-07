# Instance Methods

Instance methods are functions applied to instances of an object.

```python
class Player:
    ...
    # `move` is a method
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

The object itself is always passed as first argument.

```python
>>> a.move(1, 2)

# matches `a` to `self`
# matches `1` to `dx`
# matches `2` to `dy`
def move(self, dx, dy):
```

By convention, the instance is called `self`. However, the actual name used is unimportant. The object is always passed as the first argument. It is merely Python programming style to call this argument `self`.
