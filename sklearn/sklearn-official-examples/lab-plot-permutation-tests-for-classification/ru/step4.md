# Построение графиков результатов

Мы строим гистограмму перестановочных оценок (нулевого распределения) как для исходного набора данных iris, так и для случайно сгенерированных данных. Также указываем оценку, полученную классификатором на исходных данных, с помощью красной линии. p-значение отображается на каждом графике.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Исходные данные
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score on original\ndata: {score_iris:.2f}\n(p-value: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
_ = ax.set_ylabel("Probability density")

plt.show()

fig, ax = plt.subplots()

# Случайные данные
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score on original\ndata: {score_rand:.2f}\n(p-value: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
ax.set_ylabel("Probability density")

plt.show()
```
