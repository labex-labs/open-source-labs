# Speichern des numpy-Arrays als Pillow-Bild

Jetzt, nachdem wir das numpy-Array haben, können wir es an Pillow weitergeben und es im von Pillow unterstützten Format speichern. In diesem Beispiel speichern wir den Plot als BMP-Bild.

```python
im = Image.fromarray(rgba)
im.save("test.bmp")
```
