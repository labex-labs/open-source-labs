# Pré-processar Dados

Antes de aplicar o SGD, muitas vezes é benéfico pré-processar os dados. Neste caso, vamos padronizar as características usando o StandardScaler do scikit-learn.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
