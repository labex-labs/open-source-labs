# Misturar com Transparência

A maneira mais simples de incluir transparência ao plotar dados com `imshow` é passar um array correspondente ao formato dos dados para o argumento `alpha`.

```python
# Create an alpha channel of linearly increasing values moving to the right.
alphas = np.ones(weights.shape)
alphas[:, 30:] = np.linspace(1, 0, 70)

# Create the figure and image
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)
ax.set_axis_off()
plt.show()
```
