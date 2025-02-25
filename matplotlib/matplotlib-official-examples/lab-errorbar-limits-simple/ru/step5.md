# Создаем график с отрезками ошибок с обоими верхними и нижними пределами

В этом шаге мы создаем график с отрезками ошибок с обоими верхними и нижними пределами.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
