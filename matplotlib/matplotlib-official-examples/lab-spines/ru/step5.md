# Настройка "хребтов" (spines) для нижней и левой сторон

Во втором подграфике мы будем отображать "хребты" только на нижней и левой сторонах графика. Мы можем скрыть "хребты" на правой и верхней сторонах графика с использованием метода `set_visible`.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```