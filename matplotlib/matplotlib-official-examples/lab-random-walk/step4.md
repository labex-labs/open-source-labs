# Generate Random Walks

We generate 40 random walks with 30 steps each using the `random_walk()` function defined earlier. We store all the random walks in a list called `walks`.

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
