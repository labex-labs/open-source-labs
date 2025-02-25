# Dessiner des textes sur une figure avec positionnement en coordonnées pixels

Alternativement, nous pouvons directement dessiner du texte sur une figure avec un positionnement en coordonnées pixels en utilisant `.Figure.text` ainsi que `.transforms.IdentityTransform`.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
