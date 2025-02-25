# Определяем функцию случайного блуждания

Определяем функцию, которая генерирует случайное блуждание с заданным количеством шагов и максимальным размером шага. Функция принимает два входных параметра: `num_steps` - общее количество шагов в случайном блуждании, и `max_step` - максимальный размер каждого шага. Мы используем `numpy.random` для генерации случайных чисел для шагов и `numpy.cumsum` для вычисления накопленной суммы шагов, чтобы получить конечную позицию.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
