# Сохранение массива numpy в изображение Pillow

Теперь, когда у нас есть массив numpy, мы можем передать его в Pillow и сохранить в любом формате, поддерживаемом Pillow. В этом примере мы сохраним график в виде BMP - изображения.

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
