# Генерируем случайные данные

Мы сгенерируем два набора случайных данных с использованием функции `random.normal` библиотеки NumPy. Эти наборы будут использоваться для создания гистограмм разных стилей.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
