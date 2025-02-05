# Create Plot

Now, we can create the plot that we want to overlay the image on. In this example, we will create a simple bar plot using random data.

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```
