# ROC Multiclasses Um-contra-Um

A estratégia multiclasses Um-contra-Um (OvO) consiste em ajustar um classificador por par de classes. Como requer o treino de `n_classes` \* (`n_classes` - 1) / 2 classificadores, este método é geralmente mais lento que o Um-contra-Todos devido à sua complexidade O(`n_classes` ^2). Neste passo, mostramos como calcular a curva ROC utilizando a estratégia multiclasses OvO.

```python
pair_list = [(0, 1), (1, 2), (0, 2)]
pair_scores = []
mean_tpr = dict()

# Calcular a curva ROC e a pontuação ROC AUC para cada par de classes
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
        label=f"Média {target_names[label_a]} vs {target_names[label_b]} (AUC = {mean_score :.2f})",
        linestyle=":",
        linewidth=4,
    )
    RocCurveDisplay.from_predictions(
        a_true,
        y_score[ab_mask, idx_a],
        ax=ax,
        name=f"{target_names[label_a]} como classe positiva",
    )
    RocCurveDisplay.from_predictions(
        b_true,
        y_score[ab_mask, idx_b],
        ax=ax,
        name=f"{target_names[label_b]} como classe positiva",
        plot_chance_level=True,
    )
    plt.axis("square")
    plt.xlabel("Taxa de Falsos Positivos")
    plt.ylabel("Taxa de Verdadeiros Positivos")
    plt.title(f"{target_names[idx_a]} vs {target_names[idx_b]} Curvas ROC")
    plt.legend()
    plt.show()

# Calcular a curva ROC e a pontuação ROC AUC da média macro
mean_tpr = np.zeros_like(fpr_grid)
for ix in range(len(pair_list)):
    mean_tpr += mean_tpr[ix]
mean_tpr /= len(pair_list)

macro_roc_auc_ovo = roc_auc_score(y_test, y_score, multi_class="ovo", average="macro")

plt.plot(
    fpr_grid,
    mean_tpr,
    label=f"Curva ROC da média macro (AUC = {macro_roc_auc_ovo:.2f})",
    linestyle=":",
    linewidth=4,
)

plt.plot([0, 1], [0, 1], "k--", label="Nível de acaso")
plt.axis("square")
plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curvas ROC Um-contra-Um")
plt.legend()
plt.show()
```
