# Построение графиков результатов

Наконец, мы построим графики, показывающие, насколько хорошо наша модель работает с нашими двумя регрессорами: одним деревом решений и AdaBoost. Мы используем функцию `scatter()` библиотеки Matplotlib для построения точек обучающей выборки и предсказанных значений обоих регрессоров. Мы используем функцию `plot()` библиотеки Matplotlib для построения графиков предсказанных значений в зависимости от исходных данных для обоих регрессоров. Добавляем легенду на график, чтобы отличить между двумя регрессорами.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
```
