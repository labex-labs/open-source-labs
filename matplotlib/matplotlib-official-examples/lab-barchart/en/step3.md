# Create a Grouped Bar Chart

Now, we can create our chart using the `bar` function from Matplotlib. We will create a loop that iterates through our attributes and creates a set of bars for each one. We will also adjust the width of the bars and the position of each set of bars.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
