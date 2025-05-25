# Busca em Grade

A busca em grade é uma técnica que pode ser usada para encontrar a melhor combinação de valores de parâmetros para um estimador. Envolve especificar uma grade de valores de parâmetros, ajustar o estimador nos dados de treino para cada combinação de parâmetros e selecionar os parâmetros que resultam na maior pontuação de validação cruzada.

```python
from sklearn.model_selection import GridSearchCV

# Define uma grade de valores de parâmetros
Cs = np.logspace(-6, -1, 10)

# Cria um objeto GridSearchCV com o classificador SVM e a grade de parâmetros
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Ajusta o objeto GridSearchCV nos dados de treino
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
