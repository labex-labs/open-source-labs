# Сравнение результатов с и без раннего прекращения

Теперь мы сравним результаты двух моделей.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="Без раннего прекращения", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="С ранним прекращением", color="coral"
)

plt.xticks(index + bar_width, имена)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Наборы данных")
plt.ylabel("Результат тестирования")

plt.show()
```
