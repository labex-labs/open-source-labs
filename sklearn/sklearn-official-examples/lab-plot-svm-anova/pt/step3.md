# Plotar a Pontuação de Validação Cruzada

Plotamos a pontuação de validação cruzada em função do percentil das características.

```python
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

score_means = list()
score_stds = list()
percentiles = (1, 3, 6, 10, 15, 20, 30, 40, 60, 80, 100)

for percentile in percentiles:
    clf.set_params(anova__percentile=percentile)
    this_scores = cross_val_score(clf, X, y)
    score_means.append(this_scores.mean())
    score_stds.append(this_scores.std())

plt.errorbar(percentiles, score_means, np.array(score_stds))
plt.title("Desempenho do SVM-Anova variando o percentil das características selecionadas")
plt.xticks(np.linspace(0, 100, 11, endpoint=True))
plt.xlabel("Percentil")
plt.ylabel("Pontuação de Precisão")
plt.axis("tight")
plt.show()
```
