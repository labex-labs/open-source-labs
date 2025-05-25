# One-vs-One 다중 클래스 ROC

One-vs-One (OvO) 다중 클래스 전략은 각 클래스 쌍에 대해 하나의 분류기를 맞추는 방식입니다. `n_classes` \* (`n_classes` - 1) / 2 개의 분류기를 학습해야 하므로, O(`n_classes` ^2) 의 복잡도로 인해 One-vs-Rest 보다 일반적으로 느립니다. 이 단계에서는 OvO 다중 클래스 전략을 사용하여 ROC 곡선을 계산하는 방법을 보여줍니다.

```python
pair_list = [(0, 1), (1, 2), (0, 2)]
pair_scores = []
mean_tpr = dict()

# 각 클래스 쌍에 대한 ROC 곡선 및 ROC AUC 점수 계산
for ix, (label_a, label_b) in enumerate(pair_list):
    a_mask = y_test == target_names[label_a]
    b_mask = y_test == target_names[label_b]
    ab_mask = np.logical_or(a_mask, b_mask)

    a_true = a_mask[ab_mask]
    b_true = b_mask[ab_mask]

    idx_a = np.flatnonzero(label_binarizer.classes_ == target_names[label_a])[0]
    idx_b = np.flatnonzero(label_binarizer.classes_ == target_names[label_b])[0]

    fpr_a, tpr_a, _ = roc_curve(a_true, y_score[ab_mask, idx_a])
    fpr_b, tpr_b, _ = roc_curve(b_true, y_score[ab_mask, idx_b])

    mean_tpr[ix] = np.zeros_like(fpr_grid)
    mean_tpr[ix] += np.interp(fpr_grid, fpr_a, tpr_a)
    mean_tpr[ix] += np.interp(fpr_grid, fpr_b, tpr_b)
    mean_tpr[ix] /= 2
    mean_score = auc(fpr_grid, mean_tpr[ix])
    pair_scores.append(mean_score)

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.plot(
        fpr_grid,
        mean_tpr[ix],
        label=f"Mean {target_names[label_a]} vs {target_names[label_b]} (AUC = {mean_score :.2f})",
        linestyle=":",
        linewidth=4,
    )
    RocCurveDisplay.from_predictions(
        a_true,
        y_score[ab_mask, idx_a],
        ax=ax,
        name=f"{target_names[label_a]} as positive class",
    )
    RocCurveDisplay.from_predictions(
        b_true,
        y_score[ab_mask, idx_b],
        ax=ax,
        name=f"{target_names[label_b]} as positive class",
        plot_chance_level=True,
    )
    plt.axis("square")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"{target_names[idx_a]} vs {target_names[idx_b]} ROC curves")
    plt.legend()
    plt.show()

# 매크로 평균 ROC 곡선 및 ROC AUC 점수 계산
mean_tpr = np.zeros_like(fpr_grid)
for ix in range(len(pair_list)):
    mean_tpr += mean_tpr[ix]
mean_tpr /= len(pair_list)

macro_roc_auc_ovo = roc_auc_score(y_test, y_score, multi_class="ovo", average="macro")

plt.plot(
    fpr_grid,
    mean_tpr,
    label=f"Macro-average ROC curve (AUC = {macro_roc_auc_ovo:.2f})",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Chance level")
plt.axis("square")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("One-vs-One ROC curves")
plt.legend()
plt.show()
```
