# Why `super()`

Always use `super()` when overriding methods.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()` delegates to the _next class_ on the MRO.

The tricky bit is that you don't know what it is. You especially don't
know what it is if multiple inheritance is being used.
