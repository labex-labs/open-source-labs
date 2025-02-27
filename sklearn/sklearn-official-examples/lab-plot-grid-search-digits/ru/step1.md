# Загрузка данных

Мы загрузим датасет digits и сгладим изображения до векторов. Каждый пиксель изображения размером 8 на 8 пикселей должен быть преобразован в вектор из 64 пикселей. Таким образом, мы получим окончательный массив данных формы `(n_images, n_pixels)`. Также мы разделим данные на обучающий и тестовый наборы равного размера.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
