# Ajustar um Modelo de Mistura Gaussiana

Agora, podemos ajustar um Modelo de Mistura Gaussiana aos nossos dados usando a classe `GaussianMixture` do módulo `sklearn.mixture`. Especifique o número desejado de componentes e quaisquer outros parâmetros que desejar usar.

```python
# Ajustar um Modelo de Mistura Gaussiana
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
