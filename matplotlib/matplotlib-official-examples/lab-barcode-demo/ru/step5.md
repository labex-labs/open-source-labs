# Отображаем штрих-код

Наконец, мы можем отобразить штрих-код с использованием `Axes.imshow`. Мы будем использовать `code.reshape(1, -1)` для преобразования данных в двумерный массив с одной строкой, `imshow(..., aspect='auto')` для обеспечения неквадратных пикселей и `imshow(..., interpolation='nearest')` для предотвращения размытия краев.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
