# Создаем простую карту уровня с подписями

Теперь, когда у нас есть данные, мы можем создать простую карту уровня с подписями, используя стандартные цвета.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
