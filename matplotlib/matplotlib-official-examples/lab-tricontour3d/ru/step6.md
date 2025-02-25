# Создаем трехмерный контурный график

Мы создадим трехмерный контурный график с использованием созданной триангуляции и координат z. Также настроим угол обзора, чтобы график был легче понять.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
