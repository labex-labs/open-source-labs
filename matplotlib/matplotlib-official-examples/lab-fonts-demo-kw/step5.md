# Show font weights

Now, we will display the different font weights available in Matplotlib. We will use the `fig.text()` method to display each font weight, with the weight name as the text and the corresponding font weight as a keyword argument.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
