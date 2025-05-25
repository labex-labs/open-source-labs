# Plotando a Comparação da Seleção de Características

Podemos plotar as pontuações e pesos das características para cada uma, a fim de visualizar o impacto da seleção de características univariadas.

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"Pontuação univariada ($-Log(p_{value})$)"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="Peso SVM")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="Pesos SVM após seleção",
)

plt.title("Comparando a seleção de características")
plt.xlabel("Número da característica")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```
