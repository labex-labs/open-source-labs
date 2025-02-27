#Comparer les régresseurs

Nous traçons les données projetées sur la première composante en fonction de la cible pour les deux régresseurs PCR et PLS. Dans les deux cas, ces données projetées sont celles que les régresseurs utiliseront comme données d'entraînement.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="vérité terrain")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="prédictions"
)
axes[0].set(
    xlabel="Données projetées sur la première composante PCA", ylabel="y", titre="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="vérité terrain")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="prédictions"
)
axes[1].set(xlabel="Données projetées sur la première composante PLS", ylabel="y", titre="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

Nous affichons les scores R-carré des deux estimateurs, ce qui confirme davantage que la PLS est une meilleure alternative que la PCR dans ce cas.

```python
print(f"PCR r-carré {pcr.score(X_test, y_test):.3f}")
print(f"PLS r-carré {pls.score(X_test, y_test):.3f}")
```
