# Fall mit L1-Strafe

Im Falle der L1-Strafe besagt die Theorie, dass die Modellkonsistenz, was das Finden der richtigen Menge an nicht-null Parametern sowie ihrer Vorzeichen betrifft, durch die Skalierung von `C` erreicht werden kann. Wir demonstrieren diesen Effekt, indem wir ein synthetisches Dataset verwenden, das spars ist, was bedeutet, dass nur wenige Merkmale für das Modell informativ und nützlich sein werden.

```python
model_l1 = LinearSVC(penalty="l1", loss="squared_hinge", dual=False, tol=1e-3)

Cs = np.logspace(-2.3, -1.3, 10)
train_sizes = np.linspace(0.3, 0.7, 3)
labels = [f"Anteil: {train_size}" for train_size in train_sizes]

results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l1, X, y, param_name="C", param_range=Cs, cv=cv
    )
    results[label] = test_scores.mean(axis=1)
results = pd.DataFrame(results)

fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 6))

# Ergebnisse ohne Skalierung von C plotten
results.plot(x="C", ax=axes[0], logx=True)
axes[0].set_ylabel("CV-Score")
axes[0].set_title("Keine Skalierung")

# Ergebnisse durch Skalierung von C plotten
for train_size_idx, label in enumerate(labels):
    results_scaled = results[[label]].assign(
        C_scaled=Cs * float(n_samples * train_sizes[train_size_idx])
    )
    results_scaled.plot(x="C_scaled", ax=axes[1], logx=True, label=label)
axes[1].set_title("Skaliere C mit 1 / n_samples")

_ = fig.suptitle("Effekt der Skalierung von C mit L1-Strafe")
```
