# Plot the Text

Now that we have defined the text, we can plot it using Matplotlib. In this step, we create a figure and add the text to it using the `fig.text()` method.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i + .5) / len(tests), s, fontsize=32)

plt.show()
```
