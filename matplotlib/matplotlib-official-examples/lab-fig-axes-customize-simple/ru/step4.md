# Настройка делений и меток

Мы настроим деления и метки осей с использованием метода `ax1.tick_params()`. Мы установим цвет, поворот и размер метки по оси x, а также цвет, размер и ширину делений по оси y.

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
