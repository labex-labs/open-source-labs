# Define the property cycle and retrieve colors

Next, we need to define the property cycle and retrieve the colors from it.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
