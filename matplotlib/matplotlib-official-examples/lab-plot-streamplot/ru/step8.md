# Непрерывные линии потока

В этом шаге мы создадим поточную диаграмму с непрерывными линиями потока. Параметр `broken_streamlines` контролирует, должны ли линии потока быть разрывами, когда они превышают предел количества линий в одной ячейке сетки.

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
