# Caso de Penalidade L2

Podemos repetir um experimento semelhante com a penalidade `l2`. Neste caso, a teoria diz que, para alcançar a consistência de previsão, o parâmetro de penalidade deve ser mantido constante à medida que o número de amostras aumenta.

```python
model_l2 = LinearSVC(penalty="l2", loss="squared_hinge", dual=True)
Cs = np.logspace(-4.5, -2, 10)

labels = [f"fração: {train_size}" for train_size in train_sizes]
results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l2, X, y, param_name="C", param_range=Cs, cv=cv
    )
    results[label] = test_scores.mean(axis=1)
results = pd.DataFrame(results)

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 6))

# plotar resultados sem escalar C
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("Pontuação CV")
axes[0].set_title("Sem escala")

# plotar resultados escalando C
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("Escalando C por 1 / n_samples")

_ = fig.suptitle("Efeito da escala de C com penalidade L2")
```
