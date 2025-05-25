# Jaccard 유사도 점수 시각화

```python
model_scores = [ovr_jaccard_score] + chain_jaccard_scores
model_scores.append(ensemble_jaccard_score)

model_names = (
    "독립",
    "체인 1",
    "체인 2",
    "체인 3",
    "체인 4",
    "체인 5",
    "체인 6",
    "체인 7",
    "체인 8",
    "체인 9",
    "체인 10",
    "앙상블",
)

x_pos = np.arange(len(model_names))

fig, ax = plt.subplots(figsize=(7, 4))
ax.grid(True)
ax.set_title("분류기 체인 앙상블 성능 비교")
ax.set_xticks(x_pos)
ax.set_xticklabels(model_names, rotation="vertical")
ax.set_ylabel("Jaccard 유사도 점수")
ax.set_ylim([min(model_scores) * 0.9, max(model_scores) * 1.1])
colors = ["r"] + ["b"] * len(chain_jaccard_scores) + ["g"]
ax.bar(x_pos, model_scores, alpha=0.5, color=colors)
plt.tight_layout()
plt.show()
```
