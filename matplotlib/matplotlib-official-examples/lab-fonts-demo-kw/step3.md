# Show font styles

Now, we will display the different font styles available in Matplotlib. We will use the `fig.text()` method to display each font style, with the style name as the text and the corresponding font style as a keyword argument.

```python
fig.text(0.3, 0.9, 'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
