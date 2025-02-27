# Импорт библиотек

Сначала нам нужно импортировать необходимые библиотеки. Мы будем использовать `matplotlib` для визуализации, `datasets` и `metrics` из `sklearn` для загрузки и оценки набора данных, а также `svm` для обучения на支持向量机 (support vector machine).

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
