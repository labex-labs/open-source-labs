# Задаем параметры для набора данных с тремя смешанными Гауссовыми распределениями

В этом шаге мы задаем параметры для набора данных с тремя смешанными Гауссовыми распределениями, которые включают в себя случайное состояние, количество компонентов, количество признаков, цвета, ковариации, количество образцов и средние значения.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```
