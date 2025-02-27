# Graficar la comparación de la selección de características

Podemos graficar las puntuaciones y pesos de cada característica para ver el impacto de la selección de características univariadas.

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"Puntuación univariada ($-Log(p_{valor})$)"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="Peso de SVM")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="Pesos de SVM después de la selección",
)

plt.title("Comparando la selección de características")
plt.xlabel("Número de característica")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```
