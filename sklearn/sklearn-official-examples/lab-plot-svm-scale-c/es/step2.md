# Caso de penalización L1

En el caso de la penalización L1, la teoría dice que la consistencia del modelo, en términos de encontrar el conjunto correcto de parámetros no nulos y sus signos, se puede lograr escalando `C`. Demostramos este efecto utilizando un conjunto de datos sintético que es disperso, lo que significa que solo algunas características serán informativas y útiles para el modelo.

```python
model_l1 = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, tol=1e-3)

Cs = np.logspace(-2.3, -1.3, 10)
train_sizes = np.linspace(0.3, 0.7, 3)
labels = [f"fracción: {train_size}" for train_size in train_sizes]

results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l1, X, y, param_name="C", param_range=Cs, cv=cv
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

_ = fig.suptitle("Efecto del escalado de C con penalización L1")
```
