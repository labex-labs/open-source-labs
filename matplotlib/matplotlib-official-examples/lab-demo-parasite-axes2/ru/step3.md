# Настройка паразитной оси

Нам нужно настроить положение паразитных осей. Функция `new_fixed_axis()` используется для создания новой оси y справа от графика. Функция `toggle()` используется для включения всех делений и меток правой оси y.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
