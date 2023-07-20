# Customize boxplot statistics

We can modify any of the boxplot statistics that were computed in Step 2. In this example, we set the median of each set to the median of all the data, and double the means.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```
