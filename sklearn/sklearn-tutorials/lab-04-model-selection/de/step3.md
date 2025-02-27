# Grid-Search

Grid-Search ist eine Technik, die verwendet werden kann, um die beste Kombination von Parameternwerten für einen Schätzer zu finden. Dabei wird ein Gitter von Parameternwerten angegeben, der Schätzer für jede Kombination von Parametern auf den Trainingsdaten angepasst und diejenigen Parameter ausgewählt, die zu dem höchsten Kreuzvalidierungsscore führen.

```python
from sklearn.model_selection import GridSearchCV

# Definiere ein Gitter von Parameternwerten
Cs = np.logspace(-6, -1, 10)

# Erstelle ein GridSearchCV-Objekt mit dem SVM-Klassifizierer und dem Parametergitter
clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), n_jobs=-1)

# Passt das GridSearchCV-Objekt auf den Trainingsdaten an
clf.fit(X_digits[:1000], y_digits[:1000])

print(clf.best_score_)
print(clf.best_estimator_.C)
```
