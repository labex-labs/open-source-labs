# Salvar o Array NumPy em uma Imagem Pillow

Agora que temos o array NumPy, podemos passá-lo para o Pillow e salvá-lo em qualquer formato suportado pelo Pillow. Neste exemplo, salvaremos o gráfico como uma imagem BMP.

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
