# Change the histogram style

We can change the style of the histogram by specifying the `histtype` parameter in the `hist` function. In this example, we will create a histogram with a step curve that has a color fill.

```python
plt.hist(x, bins=20, density=True, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
```
