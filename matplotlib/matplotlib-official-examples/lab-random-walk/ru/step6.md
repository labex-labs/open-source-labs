# Создаем анимацию

Мы создаем анимацию с использованием класса `FuncAnimation` из `matplotlib.animation`. В качестве аргументов конструктора `FuncAnimation` передаем объект фигуры, функцию обновления, общее количество кадров (которое равно количеству шагов в случайных блужданиях), список всех случайных блужданий и список всех линий.

```python
# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
```
