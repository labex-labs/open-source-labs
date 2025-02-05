# Add Text to the Plot

We can add text to our plot using the text() function. In this example, we will add a LaTeX expression to the plot using the font dictionary to customize the style.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
