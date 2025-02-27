# Загрузка датасета и разделение данных

Сначала мы загрузим датасет цифр с использованием библиотеки Scikit-Learn. Этот датасет состоит из изображений размером 8x8 цифр от 0 до 9. Каждое изображение представлено в виде массива из 64 признаков. Мы разделим данные на признаки и целевую переменную.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```
