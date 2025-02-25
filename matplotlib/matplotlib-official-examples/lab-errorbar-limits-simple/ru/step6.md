# Создаем график с отрезками ошибок с подмножествами верхних и нижних пределов

В этом шаге мы создаем график с отрезками ошибок с подмножествами верхних и нижних пределов.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
