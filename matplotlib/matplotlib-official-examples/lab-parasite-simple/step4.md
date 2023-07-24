# Adding Data

We will add the data to the plot by using the `plot` function. We will assign each line to a variable so that we can reference it later.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```
