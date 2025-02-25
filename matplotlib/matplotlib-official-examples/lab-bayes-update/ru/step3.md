# Определяем класс UpdateDist

Далее мы определяем класс под названием `UpdateDist`, который будет использоваться для обновления бета-распределения при наблюдении новых данных. Класс `UpdateDist` принимает два аргумента: объект оси Matplotlib и начальную вероятность успеха.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')
```

Метод `__init__` инициализирует экземпляр класса, устанавливая начальное количество успехов равным нулю (`self.success = 0`) и начальную вероятность успеха значением, переданным в качестве аргумента (`self.prob = prob`). Мы также создаем объект линии для представления бета-распределения и настраиваем параметры графика.

Метод `__call__` вызывается каждый раз при обновлении анимации. Он моделирует эксперимент с подбрасыванием монеты и обновляет бета-распределение соответственно.

```python
def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

Если это первый кадр анимации (`if i == 0`), мы сбрасываем количество успехов до нуля и очищаем объект линии. В противном случае мы моделируем эксперимент с подбрасыванием монеты, генерируя случайное число от 0 до 1 (`np.random.rand()`) и сравнивая его с вероятностью успеха (`self.prob`). Если случайное число меньше вероятности успеха, мы считаем это успехом и обновляем бета-распределение с использованием функции `beta_pdf`. Наконец, мы обновляем объект линии новыми данными и возвращаем его.
