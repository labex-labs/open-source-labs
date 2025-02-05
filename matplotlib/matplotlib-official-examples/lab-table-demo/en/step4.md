# Create Color Scheme

We will create a color scheme for the table using the `plt.cm.BuPu` function. We will use a pastel shade of blue and purple colors for the rows.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
