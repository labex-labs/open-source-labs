# Visualiser les résultats

Nous visualisons les résultats de la validation croisée non imbriquée et imbriquée à l'aide d'un diagramme à barres.

```python
from matplotlib import pyplot as plt

# Plot bar chart of the difference.
plt.bar(["Non-Nested", "Nested"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("Score")
plt.title("Non-Nested and Nested Cross-Validation Scores")
plt.show()
```
