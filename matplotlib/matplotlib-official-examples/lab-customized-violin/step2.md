# Create a default violin plot

Next, we will create a default violin plot using Matplotlib's `violinplot` function. This will provide a baseline for comparison when we customize the plot in later steps.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
