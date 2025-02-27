# Caso de penalización L2

Podemos repetir un experimento similar con la penalización `l2`. En este caso, la teoría dice que para lograr la consistencia en la predicción, el parámetro de penalización debe mantenerse constante a medida que crece el número de muestras.

```python
model_l2 = LinearSVC(penalty="l2", loss="squared_hinge", dual=True)
Cs = np.logspace(-4.5, -2, 10)

labels = [f"fracción: {train_size}" for train_size in train_sizes]
results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l2, X, y, param_name="C", param_range=Cs, cv=cv
    )
    results[label] = test_scores.mean(axis=1)
results = pd.DataFrame(results)

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 6))

# grafica los resultados sin escalar C
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("Puntuación CV")
axes[0].set_title("Sin escalado")

# grafica los resultados escalando C
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("Escalando C por 1 / n_samples")

_ = fig.suptitle("Efecto del escalado de C con penalización L2")
```
