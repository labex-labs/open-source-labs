# Создание набора данных

Мы создаем набор данных с двумя многомерными коварирующими двухмерными наборами данных, X и Y. Затем мы извлекаем направления ковариации, то есть компоненты каждого набора данных, которые объясняют наибольшую общую дисперсию между обоими наборами данных.

```python
import numpy as np

n = 500
# 2 латентных переменные:
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

латенты = np.array([l1, l1, l2, l2]).T
X = латенты + np.random.normal(size=4 * n).reshape((n, 4))
Y = латенты + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
