# Define Random Walk Function

We define a function that generates a random walk with a given number of steps and maximum step size. The function takes two inputs: `num_steps` is the total number of steps in the random walk and `max_step` is the maximum size of each step. We use `numpy.random` to generate random numbers for the steps and `numpy.cumsum` to compute the cumulative sum of the steps to obtain the final position.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
