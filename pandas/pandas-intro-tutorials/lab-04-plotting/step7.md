# Create Subplots for Each Column

We can create separate subplots for each of the data columns using the subplots argument.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
