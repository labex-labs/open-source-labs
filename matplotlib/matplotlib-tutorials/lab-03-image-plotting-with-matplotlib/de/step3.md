# Anwenden von Pseudofarbschemata

Pseudofarbschemata können verwendet werden, um den Kontrast zu verbessern und die Daten einfacher zu visualisieren. Wenn das Bild graustufenhaft ist, können wir Pseudofarbschemata anwenden, indem wir verschiedene Farbskalen angeben. Wir können dies tun, indem wir den Parameter `cmap` in der `imshow`-Funktion verwenden.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
