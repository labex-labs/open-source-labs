# Enregistrer le tableau numpy sous forme d'image Pillow

Maintenant que nous avons le tableau numpy, nous pouvons le passer à Pillow et l'enregistrer au format pris en charge par Pillow. Dans cet exemple, nous allons enregistrer le tracé sous forme d'image BMP.

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
