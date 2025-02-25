# Добавление MultiCursor

Наконец, мы добавим функцию `MultiCursor`, чтобы отобразить курсор на всех трех графиках при наведении на точку данных.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
