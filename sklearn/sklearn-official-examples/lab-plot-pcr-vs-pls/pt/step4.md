# Comparar os Regressores

Plotamos os dados projetados no primeiro componente contra o alvo para os regressores PCR e PLS. Em ambos os casos, esses dados projetados são o que os regressores usarão como dados de treinamento.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="predictions"
)
axes[0].set(
    xlabel="Dados projetados no primeiro componente PCA", ylabel="y", title="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="ground truth")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="predictions"
)
axes[1].set(xlabel="Dados projetados no primeiro componente PLS", ylabel="y", title="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

Imprimimos as pontuações R-quadrado de ambos os estimadores, o que confirma ainda mais que o PLS é uma alternativa melhor que o PCR neste caso.

```python
print(f"PCR r-squared {pcr.score(X_test, y_test):.3f}")
print(f"PLS r-squared {pls.score(X_test, y_test):.3f}")
```
