# Criar um modelo SVM

Criaremos um modelo SVM linear com treino por Gradiente Descendente Estocástico (SGD).

```python
# criar modelo SVM com treino por SGD
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
