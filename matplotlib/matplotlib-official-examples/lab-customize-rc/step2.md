# Customize Default Parameters

To customize the default parameters for a specific figure, you can use the `rcParams.update()` method again. This time, you'll pass a dictionary of parameter names and values that you want to set for that figure. Here's an example that sets some default parameters for a specific figure:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
