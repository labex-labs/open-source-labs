# Создаем анимацию

Теперь мы создадим анимацию с использованием метода ArtistAnimation. Мы передадим в него объект figure, список ims, интервал между кадрами и задержку повторения.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
