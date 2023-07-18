# Show font sizes

Finally, we will display the different font sizes available in Matplotlib. We will use the `fig.text()` method to display each font size, with the size name as the text and the corresponding font size as a keyword argument.

```python
fig.text(0.9, 0.9, 'size', **alignment)
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
