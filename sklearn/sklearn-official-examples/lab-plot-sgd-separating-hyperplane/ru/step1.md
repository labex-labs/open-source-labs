# Импортируем необходимые библиотеки и генерируем данные

Во - первых, нам нужно импортировать необходимые библиотеки и сгенерировать набор данных, подходящий для классификации. В этом примере мы сгенерируем 50 разделимых точек с использованием функции `make_blobs` из Scikit - learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# мы создаем 50 разделимых точек
X, Y = make_blobs(n_samples = 50, centers = 2, random_state = 0, cluster_std = 0.60)
```
