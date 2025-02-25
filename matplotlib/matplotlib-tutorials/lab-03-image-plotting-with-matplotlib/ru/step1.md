# Импорт изображений

Для начала нам нужно импортировать необходимые библиотеки и загрузить изображение в массив NumPy. В нашем случае мы будем использовать библиотеку `PIL` для загрузки изображения, а затем преобразовать его в массив NumPy.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
