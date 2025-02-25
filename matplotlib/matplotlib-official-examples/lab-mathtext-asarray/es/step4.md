# Dibujar textos en una figura con posicionamiento en coordenadas de píxeles

Alternativamente, podemos dibujar directamente texto en una figura con posicionamiento en coordenadas de píxeles usando `.Figure.text` junto con `.transforms.IdentityTransform`.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
