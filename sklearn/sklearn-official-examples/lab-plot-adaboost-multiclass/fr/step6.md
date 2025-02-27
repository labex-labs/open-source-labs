# Tracer les résultats

Nous allons tracer l'erreur de test, l'erreur de classification et le poids d'amorçage de chaque modèle.

```python
n_trees_discrete = len(bdt_discrete)
n_trees_real = len(bdt_real)

# L'amorçage peut se terminer tôt, mais les tableaux suivants sont toujours
# de longueur n_estimators. Nous les réduisons au nombre réel d'arbres ici :
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
plt.ylabel("Erreur de test")
plt.xlabel("Nombre d'arbres")

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
plt.ylabel("Erreur")
plt.xlabel("Nombre d'arbres")
plt.ylim((0.2, max(real_estimator_errors.max(), discrete_estimator_errors.max()) * 1.2))
plt.xlim((-20, len(bdt_discrete) + 20))

plt.subplot(133)
plt.plot(range(1, n_trees_discrete + 1), discrete_estimator_weights, "b", label="SAMME")
plt.legend()
plt.ylabel("Poids")
plt.xlabel("Nombre d'arbres")
plt.ylim((0, discrete_estimator_weights.max() * 1.2))
plt.xlim((-20, n_trees_discrete + 20))

# Empêcher les étiquettes des axes y de se chevaucher
plt.subplots_adjust(wspace=0.25)
plt.show()
```
