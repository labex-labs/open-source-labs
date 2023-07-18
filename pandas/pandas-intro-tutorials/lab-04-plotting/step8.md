# Customize and Save the Plot

We can further customize the plot using Matplotlib's customization options. We can also save the plot to a file.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
