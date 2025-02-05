# Plot the graph

Now that we have our example data, we can plot the graph using the `errorbar()` function. We will pass in the `x` and `y` arrays as the first two parameters. We will then specify the error in the x-direction as 0.2 and the error in the y-direction as 0.4 using the `xerr` and `yerr` parameters, respectively.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
