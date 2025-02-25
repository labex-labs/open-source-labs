# Определить GridHelperCurveLinear

Третий шаг - это определить экземпляр GridHelperCurveLinear. Мы будем использовать функции преобразования, определённые на втором шаге, для преобразования сетки. Также мы установим `grid_locator1` и `grid_locator2` в `MaxNLocator(nbins=6)`, чтобы увеличить плотность делений шкалы.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
