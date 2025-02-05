# Create the Plot

Next, we will create the plot using Matplotlib's `subplots()` function and plot the adjusted close price of Google's stock over time.

```python
fig, ax = plt.subplots()
ax.plot(r.date, r.adj_close)
```
