# Создаем анимацию

Теперь мы создадим анимацию с использованием функции FuncAnimation из Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
