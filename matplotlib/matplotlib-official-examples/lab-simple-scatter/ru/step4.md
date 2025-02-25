# Создание анимации

Последним шагом является создание анимации. Мы это делаем с использованием функции FuncAnimation из модуля animation. Эта функция принимает несколько аргументов, в том числе объект фигуры, функцию, которая будет обновлять график, и количество кадров для использования.

```python
def animate(i):
    scat.set_offsets((x[i], 0))
    return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x) - 1, interval=50)
```
