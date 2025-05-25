# Prever Probabilidades de Classe para todos os Classificadores

Preveremos as probabilidades de classe para todos os classificadores usando a função `predict_proba()`.

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
