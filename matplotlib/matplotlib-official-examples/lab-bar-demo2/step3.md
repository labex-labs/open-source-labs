# Create the Bar Graph with Default Units

In this step, we will create the bar graph with default units using Matplotlib's `bar` method. We will use the `bottom` parameter to set the bottom of the bars to 0.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
