# Show font variants

Next, we will display the different font variants available in Matplotlib. We will use the `fig.text()` method to display each font variant, with the variant name as the text and the corresponding font variant as a keyword argument.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal', 'small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
