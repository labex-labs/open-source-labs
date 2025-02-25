# Создание графика

Теперь мы создадим график с использованием функции `tricontourf()` и настроим угол обзора.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
