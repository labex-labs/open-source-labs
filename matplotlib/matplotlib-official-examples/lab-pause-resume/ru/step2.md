# Определение анимации

В этом шаге мы определим анимацию, которую хотим создать. Мы создадим анимацию, которая отображает нормальное распределение, которое движется вправо на каждом кадре.

```python
class PauseAnimation:
    def __init__(self):
        # Создаем фигуру и ось
        fig, ax = plt.subplots()
        ax.set_title('Click to pause/resume the animation')

        # Создаем значения оси x
        x = np.linspace(-0.1, 0.1, 1000)

        # Начинаем с нормального распределения
        self.n0 = (1.0 / ((4 * np.pi * 2e-4 * 0.1) ** 0.5)
                   * np.exp(-x ** 2 / (4 * 2e-4 * 0.1)))

        # Создаем график
        self.p, = ax.plot(x, self.n0)

        # Создаем анимацию
        self.animation = animation.FuncAnimation(
            fig, self.update, frames=200, interval=50, blit=True)

        # Устанавливаем анимацию как непрерывную
        self.paused = False

        # Добавляем событие нажатия кнопки для переключения между паузой и работой
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def toggle_pause(self, *args, **kwargs):
        # Переключаемся между паузой и работой
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, i):
        # Обновляем нормальное распределение
        self.n0 += i / 100 % 5
        self.p.set_ydata(self.n0 % 20)
        return (self.p,)
```
