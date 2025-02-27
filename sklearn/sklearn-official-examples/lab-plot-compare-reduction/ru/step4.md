# Построение графиков результатов

Построим результаты `GridSearchCV` с использованием столбчатой диаграммы. Это позволит сравнить точность различных методов уменьшения размерности признаков.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# оценки расположены в порядке итерации param_grid, то есть в алфавитном порядке
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# выбираем оценку для наилучшего значения C
mean_scores = mean_scores.max(axis=0)
# создаем DataFrame для удобства построения графика
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Сравнение методов уменьшения размерности признаков")
ax.set_xlabel("Уменьшенное количество признаков")
ax.set_ylabel("Точность классификации цифр")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```
