# Определение значений гиперпараметров для тестирования

Мы будем тестировать разные значения параметра регуляризации C, который контролирует компромисс между максимизацией отступа и минимизацией ошибки классификации. Мы будем тестировать 10 значений, расположенных логарифмически между 10^-10 и 1.

```python
C_s = np.logspace(-10, 0, 10)
```
