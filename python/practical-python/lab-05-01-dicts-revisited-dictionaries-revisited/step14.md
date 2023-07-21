# An Odd Code Reuse (Involving Multiple Inheritance)

Consider two completely unrelated objects:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
```

And

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
```

There is a code commonality in the implementation of `LoudDog.noise()` and
`LoudBike.noise()`. In fact, the code is exactly the same. Naturally,
code like that is bound to attract software engineers.
