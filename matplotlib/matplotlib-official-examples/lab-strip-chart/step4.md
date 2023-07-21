# Create the Emitter Function

The emitter function generates the data that will be passed to the update method. In this case, we are generating random data with a probability of 0.1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```
