# Customize the histogram

We can customize the histogram by changing the color, transparency, and edge color of the bars using the `color`, `alpha`, and `edgecolor` parameters.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
