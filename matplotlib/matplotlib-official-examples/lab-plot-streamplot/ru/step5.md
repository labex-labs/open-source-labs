# Переменная ширина линии

В этом шаге мы создадим поточную диаграмму с изменяемой шириной линии. Параметр `linewidth` контролирует ширину линий потока. Здесь мы используем массив `speed`, который мы вычисляли ранее, чтобы изменить ширину линии.

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
