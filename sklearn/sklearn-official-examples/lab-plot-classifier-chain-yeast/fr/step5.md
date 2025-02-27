# Tracer les scores de similarité de Jaccard

```python
model_scores = [ovr_jaccard_score] + chain_jaccard_scores
model_scores.append(ensemble_jaccard_score)

model_names = (
    "Independent",
    "Chaîne 1",
    "Chaîne 2",
    "Chaîne 3",
    "Chaîne 4",
    "Chaîne 5",
    "Chaîne 6",
    "Chaîne 7",
    "Chaîne 8",
    "Chaîne 9",
    "Chaîne 10",
    "Ensemble",
)

x_pos = np.arange(len(model_names))

fig, ax = plt.subplots(figsize=(7, 4))
ax.grid(True)
ax.set_title("Comparaison des performances de l'ensemble de chaînes de classifieurs")
ax.set_xticks(x_pos)
ax.set_xticklabels(model_names, rotation="vertical")
ax.set_ylabel("Score de similarité de Jaccard")
ax.set_ylim([min(model_scores) * 0.9, max(model_scores) * 1.1])
colors = ["r"] + ["b"] * len(chain_jaccard_scores) + ["g"]
ax.bar(x_pos, model_scores, alpha=0.5, color=colors)
plt.tight_layout()
plt.show()
```
