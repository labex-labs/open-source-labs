# Generate the histogram data

Now that we have our random data, we can generate a histogram using numpy. We will use 50 bins to create our histogram. Add the following code:

```python
n, bins = np.histogram(data, 50)
```
