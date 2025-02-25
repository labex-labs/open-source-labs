# Texte auf eine Figur mit Positionierung in Pixel-Koordinaten zeichnen

Alternativ können wir Text direkt auf eine Figur mit Positionierung in Pixel-Koordinaten zeichnen, indem wir `.Figure.text` zusammen mit `.transforms.IdentityTransform` verwenden.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
