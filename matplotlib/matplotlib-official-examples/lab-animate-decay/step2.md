# Create the data generator function

Next, we need to create a function to generate the data for the animation. The function will produce a sine wave that decays over time. We will use the `itertools.count()` function to generate an infinite sequence of numbers. We will use these numbers to calculate the values of the sine wave.

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
