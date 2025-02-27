# Mehrdimensionale Merkmalsimputation mit IterativeImputer

Die Klasse `IterativeImputer` ist ein fortgeschrittener Ansatz zur Imputation fehlender Werte. Sie modelliert jedes Merkmal mit fehlenden Werten als Funktion anderer Merkmale und verwendet diese Schätzung zur Imputation. Sie lernt iterativ die Beziehungen zwischen den Merkmalen und imputiert die fehlenden Werte auf der Grundlage dieser Beziehungen.

```python
imp = IterativeImputer()
X = [[1, 2], [3, 6], [4, 8], [np.nan, 3], [7, np.nan]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [np.nan, 6]]
imputed_X_test = imp.transform(X_test)
```
