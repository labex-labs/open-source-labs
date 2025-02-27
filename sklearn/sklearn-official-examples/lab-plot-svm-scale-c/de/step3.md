# Fall mit L2-Strafe

Wir können ein ähnliches Experiment mit der `l2`-Strafe wiederholen. In diesem Fall besagt die Theorie, dass um die Vorhersagekonsistenz zu erreichen, der Strafparameter konstant gehalten werden sollte, wenn die Anzahl der Proben zunimmt.

```python
model_l2 = LinearSVC(penalty="l2", loss="squared_hinge", dual=True)
Cs = np.logspace(-4.5, -2, 10)

labels = [f"Anteil: {train_size}" for train_size in train_sizes]
results = {"C": Cs}
for label, train_size in zip(labels, train_sizes):
    cv = ShuffleSplit(train_size=train_size, test_size=0.3, n_splits=50, random_state=1)
    train_scores, test_scores = validation_curve(
        model_l2, X, y, param_name="C", param_range=Cs, cv=cv
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

_ = fig.suptitle("Effekt der Skalierung von C mit L2-Strafe")
```
