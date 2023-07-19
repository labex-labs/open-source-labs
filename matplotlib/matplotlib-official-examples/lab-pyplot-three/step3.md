# Plot the Data

In this step, we will use the `plot` function in Matplotlib to plot all three datasets in a single call. We will use red dashes for the first dataset, blue squares for the second dataset, and green triangles for the third dataset.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
