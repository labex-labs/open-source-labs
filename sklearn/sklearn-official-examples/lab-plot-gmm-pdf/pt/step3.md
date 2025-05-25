# Ajustar o Modelo de Mistura Gaussiana

Agora, ajustaremos um modelo de mistura gaussiana (GMM) aos dados usando a classe GaussianMixture do scikit-learn. Definiremos o número de componentes para 2 e o tipo de covariância para "full".

```python
# ajustar um Modelo de Mistura Gaussiana com dois componentes
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
