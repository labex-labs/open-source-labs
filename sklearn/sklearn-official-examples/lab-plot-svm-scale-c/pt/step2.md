# Caso de Penalidade L1

No caso L1, a teoria afirma que a consistência do modelo, em termos de encontrar o conjunto correto de parâmetros não nulos e seus sinais, pode ser alcançada escalando `C`. Demonstramos esse efeito usando um conjunto de dados sintético esparso, o que significa que apenas algumas características serão informativas e úteis para o modelo.

```python
model_l1 = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, tol=1e-3)

Cs = np.logspace(-2.3, -1.3, 10)
train_sizes = np.linspace(0.3, 0.7, 3)
labels = [f"fração: {train_size}" for train_size in train_sizes]

results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l1, X, y, param_name="C", param_range=Cs, cv=cv
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

_ = fig.suptitle("Efeito da escala de C com penalidade L1")
```
