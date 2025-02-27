# Daten vorverarbeiten

Wir werden die Daten normalisieren, indem wir jeden Pixelwert durch 255,0 dividieren, was der maximale Pixelwert ist.

```python
X = X / 255.0
```