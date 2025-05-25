# Prever a Pertinência a Clusters para Instâncias Desconhecidas

Neste passo, usaremos o modelo de aprendizagem indutiva para prever a pertença a clusters das novas amostras geradas. Usaremos a função `predict` da classe `InductiveClusterer` e plotaremos as novas amostras com seus clusters prováveis.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classificar instâncias desconhecidas")
```
