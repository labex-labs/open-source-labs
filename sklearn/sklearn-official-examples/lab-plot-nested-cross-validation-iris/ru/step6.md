# Визуализация результатов

Мы визуализируем результаты не-вложенной и вложенной кросс-валидации с помощью столбчатой диаграммы.

```python
from matplotlib import pyplot as plt

# Plot bar chart of the difference.
plt.bar(["Non-Nested", "Nested"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("Score")
plt.title("Non-Nested and Nested Cross-Validation Scores")
plt.show()
```
