# Combine Display Objects into a Single Plot

The display objects store the computed values that were passed as arguments. This allows for the visualizations to be easily combined using Matplotlib's API. In the following example, we place the displays next to each other in a row.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
