# Plotar as pontuações de similaridade Jaccard

```python
model_scores = [ovr_jaccard_score] + chain_jaccard_scores
model_scores.append(ensemble_jaccard_score)

model_names = (
    "Independente",
    "Cadeia 1",
    "Cadeia 2",
    "Cadeia 3",
    "Cadeia 4",
    "Cadeia 5",
    "Cadeia 6",
    "Cadeia 7",
    "Cadeia 8",
    "Cadeia 9",
    "Cadeia 10",
    "Conjunto",
)

x_pos = np.arange(len(model_names))

fig, ax = plt.subplots(figsize=(7, 4))
ax.grid(True)
ax.set_title("Comparação de Desempenho do Conjunto de Cadeias de Classificadores")
ax.set_xticks(x_pos)
ax.set_xticklabels(model_names, rotation="vertical")
ax.set_ylabel("Pontuação de Similaridade Jaccard")
ax.set_ylim([min(model_scores) * 0.9, max(model_scores) * 1.1])
colors = ["r"] + ["b"] * len(chain_jaccard_scores) + ["g"]
ax.bar(x_pos, model_scores, alpha=0.5, color=colors)
plt.tight_layout()
plt.show()
```
