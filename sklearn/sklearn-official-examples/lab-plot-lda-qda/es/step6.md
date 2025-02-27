# Visualizar los límites de decisión

Utilizaremos los conjuntos de datos generados en el Paso 1 para visualizar los límites de decisión para el LDA y el QDA.

```python
plt.figure(figsize=(10, 8), facecolor="white")
plt.suptitle("Análisis Discriminante Lineal vs Análisis Discriminante Cuadrático", y=0.98, fontsize=15)

for i, (X, y) in enumerate([dataset_fixed_cov(), dataset_cov()]):
    # Análisis Discriminante Lineal
    lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
    y_pred = lda.fit(X, y).predict(X)
    splot = plot_data(lda, X, y, y_pred, fig_index=2 * i + 1)
    plot_lda_cov(lda, splot)
    plt.axis("tight")

    # Análisis Discriminante Cuadrático
    qda = QuadraticDiscriminantAnalysis(store_covariance=True)
    y_pred = qda.fit(X, y).predict(X)
    splot = plot_data(qda, X, y, y_pred, fig_index=2 * i + 2)
    plot_qda_cov(qda, splot)
    plt.axis("tight")

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
```
