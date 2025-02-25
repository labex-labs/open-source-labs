# Array-Interpolationsschemata

Beim Ändern der Größe eines Bildes ist es erforderlich, die Pixelwerte zu interpolieren, um den fehlenden Raum zu füllen. Verschiedene Interpolationsschemata können verwendet werden, um den Wert eines Pixels anhand seiner umgebenden Pixel zu bestimmen. Matplotlib bietet verschiedene Interpolationsoptionen wie "nearest", "bilinear" und "bicubic" an.

```python
plt.imshow(img, interpolation="bilinear")
```