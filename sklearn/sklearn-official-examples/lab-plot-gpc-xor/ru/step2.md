# Создание набора данных XOR

В этом шаге мы создадим набор данных XOR с использованием numpy. Мы будем использовать функцию logical_xor для создания меток на основе входных признаков.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-3, 3, 50))
rng = np.random.RandomState(0)
X = rng.randn(200, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
