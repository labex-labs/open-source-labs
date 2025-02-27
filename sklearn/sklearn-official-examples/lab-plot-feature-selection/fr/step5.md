# Tracer la comparaison de la sélection de caractéristiques

Nous pouvons tracer les scores et les poids des caractéristiques pour chaque caractéristique pour voir l'impact de la sélection de caractéristiques univariées.

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"Score univarié ($-Log(p_{valeur})$)"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="Poids SVM")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="Poids SVM après sélection",
)

plt.title("Comparaison de la sélection de caractéristiques")
plt.xlabel("Numéro de la caractéristique")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```
