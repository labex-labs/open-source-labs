# Переменный цвет

В этом шаге мы создадим поточную диаграмму с изменяющимся цветом. Параметр `color` принимает двумерный массив, представляющий величину векторного поля. Здесь мы используем компоненту `U` векторного поля в качестве цвета.

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
