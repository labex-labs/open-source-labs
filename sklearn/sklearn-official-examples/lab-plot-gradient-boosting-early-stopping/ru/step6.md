# Сравнение времени обучения с и без раннего прекращения

Теперь мы сравним время обучения двух моделей.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="Без раннего прекращения", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="С ранним прекращением", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, имена)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Наборы данных")
plt.ylabel("Время обучения")

plt.show()
```
