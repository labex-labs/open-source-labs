# Define the Sine Wave Function

Next, we will define the function that will generate our sine wave. The function will take in two parameters, amplitude and frequency, and return the sine wave at a given time.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
