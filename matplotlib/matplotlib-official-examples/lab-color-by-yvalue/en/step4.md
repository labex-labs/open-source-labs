# Create Plot

In this step, we will create the plot using the masked arrays created in the previous step. We will plot each masked array separately and use different colors for each.

```python
fig, ax = plt.subplots()
ax.plot(t, smiddle, t, slower, t, supper)
plt.show()
```
