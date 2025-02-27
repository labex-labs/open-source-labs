# Hyperparameter-Tuning

Wir verwenden RandomizedSearchCV, um das Raster (Grid) der Hyperparameter zu erkunden und die beste Kombination von Hyperparametern für die Pipeline (Bearbeitungsreihenfolge) zu finden. In diesem Fall setzen wir n_iter=40, um den Suchraum zu begrenzen. Wir können n_iter erhöhen, um eine informativere Analyse zu erhalten, aber dies erhöht die Rechenzeit.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```
