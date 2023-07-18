# Adding Text

In this step, we will add text to the plot using the `text()` function.

```python
tex = r'$\mathcal{R}\prod_{i=\alpha_{i+1}}^\infty a_i\sin(2 \pi f x_i)$'
ax.text(1, 1.6, tex, fontsize=20, va='bottom')
```
