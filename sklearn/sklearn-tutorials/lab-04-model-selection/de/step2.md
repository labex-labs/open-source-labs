# Kreuzvalidierungsgeneratoren

Scikit-learn bietet eine Sammlung von Klassen an, die verwendet werden können, um Trainings-/Test-Indizes für beliebte Kreuzvalidierungsstrategien zu generieren. Diese Klassen haben eine `split`-Methode, die den Eingabedatensatz akzeptiert und die Trainings-/Test-Set-Indizes für jede Iteration des Kreuzvalidierungsprozesses liefert.

```python
from sklearn.model_selection import KFold

# Teile die Daten in K Folds auf, indem die KFold-Kreuzvalidierung verwendet wird
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

Die Hilfsfunktion `cross_val_score` kann verwendet werden, um den Kreuzvalidierungsscore direkt zu berechnen. Sie teilt die Daten in Trainings- und Testsets für jede Iteration der Kreuzvalidierung auf, trainiert den Schätzer auf dem Trainingsset und berechnet den Score basierend auf dem Testset.

```python
from sklearn.model_selection import cross_val_score

# Berechne den Kreuzvalidierungsscore für den SVM-Klassifizierer
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
