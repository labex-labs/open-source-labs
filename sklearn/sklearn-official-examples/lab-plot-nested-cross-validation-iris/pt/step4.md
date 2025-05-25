# Validação Cruzada Não Aninhada

Utilizamos validação cruzada não aninhada para ajustar os hiperparâmetros e avaliar o desempenho do modelo. A função `GridSearchCV` realiza uma busca exaustiva sobre valores de parâmetros especificados para um estimador. Usamos uma validação cruzada de 4 dobras.

```python
from sklearn.model_selection import GridSearchCV

# Busca de parâmetros não aninhada e pontuação
clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=4)
clf.fit(X_iris, y_iris)
non_nested_score = clf.best_score_
```
