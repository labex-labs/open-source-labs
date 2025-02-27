# Zeichnen der Ergebnisse

Wir werden die Testfehler, die Klassifikationsfehler und das Boost-Gewicht jedes Modells zeichnen.

```python
n_trees_discrete = len(bdt_discrete)
n_trees_real = len(bdt_real)

# Boosting kann frühzeitig beendet werden, aber die folgenden Arrays sind immer
# n_estimators lang. Wir schneiden sie hier auf die tatsächliche Anzahl von Bäumen ab:
discrete_estimator_errors = bdt_discrete.estimator_errors_[:n_trees_discrete]
real_estimator_errors = bdt_real.estimator_errors_[:n_trees_real]
discrete_estimator_weights = bdt_discrete.estimator_weights_[:n_trees_discrete]

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(range(1, n_trees_discrete + 1), discrete_test_errors, c="black", label="SAMME")
plt.plot(
    range(1, n_trees_real + 1),
    real_test_errors,
    c="black",
    linestyle="dashed",
    label="SAMME.R",
)
plt.legend()
plt.ylim(0.18, 0.62)
plt.ylabel("Testfehler")
plt.xlabel("Anzahl der Bäume")

plt.subplot(132)
plt.plot(
    range(1, n_trees_discrete + 1),
    discrete_estimator_errors,
    "b",
    label="SAMME",
    alpha=0.5,
)
plt.plot(
    range(1, n_trees_real + 1), real_estimator_errors, "r", label="SAMME.R", alpha=0.5
)
plt.legend()
plt.ylabel("Fehler")
plt.xlabel("Anzahl der Bäume")
plt.ylim((0.2, max(real_estimator_errors.max(), discrete_estimator_errors.max()) * 1.2))
plt.xlim((-20, len(bdt_discrete) + 20))

plt.subplot(133)
plt.plot(range(1, n_trees_discrete + 1), discrete_estimator_weights, "b", label="SAMME")
plt.legend()
plt.ylabel("Gewicht")
plt.xlabel("Anzahl der Bäume")
plt.ylim((0, discrete_estimator_weights.max() * 1.2))
plt.xlim((-20, n_trees_discrete + 20))

# verhindert überlappende y-Achsenbeschriftungen
plt.subplots_adjust(wspace=0.25)
plt.show()
```
