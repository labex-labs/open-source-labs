# Show font families

Next, we will display the different font families available in Matplotlib. We will use the `fig.text()` method to display each font family, with the family name as the text and the corresponding font family as a keyword argument.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
