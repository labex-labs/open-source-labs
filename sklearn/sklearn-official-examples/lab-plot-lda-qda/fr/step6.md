# Visualiser les limites de décision

Nous allons utiliser les jeux de données générés dans l'Étape 1 pour visualiser les limites de décision pour l'Analyse Discriminante Linéaire (LDA) et l'Analyse Discriminante Quadratique (QDA).

```python
plt.figure(figsize=(10, 8), facecolor="white")
plt.suptitle("Linear Discriminant Analysis vs Quadratic Discriminant Analysis", y=0.98, fontsize=15)

for i, (X, y) in enumerate([dataset_fixed_cov(), dataset_cov()]):
    # Linear Discriminant Analysis
    lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
    y_pred = lda.fit(X, y).predict(X)
    splot = plot_data(lda, X, y, y_pred, fig_index=2 * i + 1)
    plot_lda_cov(lda, splot)
    plt.axis("tight")

    # Quadratic Discriminant Analysis
    qda = QuadraticDiscriminantAnalysis(store_covariance=True)
    y_pred = qda.fit(X, y).predict(X)
    splot = plot_data(qda, X, y, y_pred, fig_index=2 * i + 2)
    plot_qda_cov(qda, splot)
    plt.axis("tight")

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
```
