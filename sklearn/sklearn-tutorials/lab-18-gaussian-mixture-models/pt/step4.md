# Agrupar os dados

Depois de o modelo ter sido ajustado, podemos utilizá-lo para agrupar os dados, atribuindo cada amostra ao componente gaussiano a que pertence. O método `predict` da classe `GaussianMixture` pode ser usado para este propósito.

```python
# Agrupar os dados
cluster_labels = gmm.predict(X_test)
```
