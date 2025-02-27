# Загрузка данных

Сначала мы загружаем набор данных digits из scikit-learn. Этот набор данных содержит изображения цифр 8x8 от 0 до 9. Мы будем использовать Анализ главных компонент (PCA), чтобы уменьшить размерность набора данных до 15.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# load the digits dataset
digits = load_digits()

# reduce the dimension of the dataset to 15 using PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
