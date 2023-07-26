# Plot the Data with \dfrac

We will plot the data with the \dfrac TeX macro and display the resulting plot.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
