# Plot Variable, Asymmetric Error Bars

Next, we will plot our data with variable, asymmetric error bars. The `ax.errorbar()` function is used again, but this time the `xerr` parameter is used to specify the asymmetric error values.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
