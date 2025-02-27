# Führen Sie eine Grid-Search mit Kreuzvalidierung durch

Die Grid-Search sucht erschöpfend durch alle möglichen Kombinationen von Hyperparametern im angegebenen Parameterrahmen. Sie bewertet die Leistung jeder Kombination mithilfe der Kreuzvalidierung.

```python
# Erstelle eine Instanz von GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Passt die Daten an, um die Grid-Search durchzuführen
grid_search.fit(X, y)

# Druckt die beste Kombination von Hyperparametern
print('Best hyperparameters:', grid_search.best_params_)
```
