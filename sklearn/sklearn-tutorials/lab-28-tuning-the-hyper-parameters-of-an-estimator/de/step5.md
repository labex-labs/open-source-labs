# Führen Sie eine zufällige Suche mit Kreuzvalidierung durch

Die zufällige Suche wählt zufällig eine Teilmenge des Parameterrahmens aus und bewertet die Leistung jeder Kombination mithilfe der Kreuzvalidierung. Sie ist nützlich, wenn der Parameterspace groß ist und eine erschöpfende Suche nicht durchführbar ist.

```python
# Erstelle eine Instanz von RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Passt die Daten an, um die zufällige Suche durchzuführen
random_search.fit(X, y)

# Druckt die beste Kombination von Hyperparametern
print('Best hyperparameters:', random_search.best_params_)
```
