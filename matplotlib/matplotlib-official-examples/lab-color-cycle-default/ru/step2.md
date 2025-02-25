# Определяем цикл свойств и извлекаем цвета

Далее, нам нужно определить цикл свойств и извлечь цвета из него.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
