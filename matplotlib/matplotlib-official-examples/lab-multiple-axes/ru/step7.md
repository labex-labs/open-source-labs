# Создать анимацию

Седьмой шаг - создать объект анимации с использованием функции `FuncAnimation`. Мы передаем в нее объект фигуры, функцию для анимации, интервал между кадрами в миллисекундах, количество кадров и задержку перед повторением анимации.

```python
ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
```
