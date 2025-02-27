# Генерация синтетического датасета

Сначала мы генерируем датасет, в котором количество выборок меньше общего количества признаков. Это приводит к недоопределенной системе, то есть решение не является уникальным, и мы не можем применить обычные наименьшие квадраты самостоятельно. Регуляризация вводит штрафную функцию в функцию целевого функционала, которая изменяет задачу оптимизации и может помочь облегчить недоопределенность системы. Мы сгенерируем целевую переменную `y`, которая является линейной комбинацией синусоидальных сигналов с чередующимися знаками. Только 10 наименьших из 100 частот в `X` используются для генерации `y`, в то время как остальные признаки не несут информации. Это приводит к высокомерному разреженному пространству признаков, где некоторое程度的 L1-штрафование необходимо.

```python
import numpy as np

rng = np.random.RandomState(0)
n_samples, n_features, n_informative = 50, 100, 10
time_step = np.linspace(-2, 2, n_samples)
freqs = 2 * np.pi * np.sort(rng.rand(n_features)) / 0.01
X = np.zeros((n_samples, n_features))

for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step)

idx = np.arange(n_features)
true_coef = (-1) ** idx * np.exp(-idx / 10)
true_coef[n_informative:] = 0  # sparsify coef
y = np.dot(X, true_coef)

# introduce random phase using numpy.random.random_sample
# add some gaussian noise using numpy.random.normal
for i in range(n_features):
    X[:, i] = np.sin(freqs[i] * time_step + 2 * (rng.random_sample() - 0.5))
    X[:, i] += 0.2 * rng.normal(0, 1, n_samples)

y += 0.2 * rng.normal(0, 1, n_samples)

# split the data into train and test sets using train_test_split from sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=False)
```
