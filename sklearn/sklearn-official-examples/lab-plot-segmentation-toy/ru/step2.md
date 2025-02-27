# Преобразование изображения в граф

Мы будем использовать `img_to_graph` из `sklearn.feature_extraction.image` для преобразования изображения в граф. Также будет вычислено значение градиента на ребрах.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
