# Comparar los regresores

Graficamos los datos proyectados sobre el primer componente en función de la variable objetivo para ambos regresores PCR y PLS. En ambos casos, estos datos proyectados son los que los regresores utilizarán como datos de entrenamiento.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].scatter(pca.transform(X_test), y_test, alpha=0.3, label="verdadero valor")
axes[0].scatter(
    pca.transform(X_test), pcr.predict(X_test), alpha=0.3, label="predicciones"
)
axes[0].set(
    xlabel="Datos proyectados sobre el primer componente PCA", ylabel="y", título="PCR / PCA"
)
axes[0].legend()
axes[1].scatter(pls.transform(X_test), y_test, alpha=0.3, label="verdadero valor")
axes[1].scatter(
    pls.transform(X_test), pls.predict(X_test), alpha=0.3, label="predicciones"
)
axes[1].set(xlabel="Datos proyectados sobre el primer componente PLS", ylabel="y", título="PLS")
axes[1].legend()
plt.tight_layout()
plt.show()
```

Imprimimos las puntuaciones de coeficiente de determinación ($R^2$) de ambos estimadores, lo que confirma aún más que la PLS es una mejor alternativa que la PCR en este caso.

```python
print(f"Coeficiente de determinación de PCR {pcr.score(X_test, y_test):.3f}")
print(f"Coeficiente de determinación de PLS {pls.score(X_test, y_test):.3f}")
```
