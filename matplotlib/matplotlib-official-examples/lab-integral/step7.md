# Add axis labels and tick labels

Add the x and y-axis labels using `figtext`. Hide the top and right spines using `spines`. Set custom tick placement and labels using `set_xticks` and `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
