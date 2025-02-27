# Vergleiche die Regressoren

Wir plotten die projizierten Daten auf die erste Komponente gegen das Ziel für beide Regressoren PCR und PLS. In beiden Fällen sind diese projizierten Daten diejenigen, die die Regressoren als Trainingsdaten verwenden werden.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="predictions"
)
axes[0].set(
    xlabel="Projizierte Daten auf die erste PCA-Komponente", ylabel="y", title="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="predictions"
)
axes[1].set(xlabel="Projizierte Daten auf die erste PLS-Komponente", ylabel="y", title="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

Wir drucken die R²-Werte beider Schätzer aus, was weiterhin bestätigt, dass PLS in diesem Fall eine bessere Alternative als PCR ist.

```python
print(f"PCR r-squared {pcr.score(X_test, y_test):.3f}")
print(f"PLS r-squared {pls.score(X_test, y_test):.3f}")
```
