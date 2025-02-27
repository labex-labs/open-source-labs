# Teilen des Datensatzes in Trainings- und Testsets

Um die Leistung unseres Modells zu evaluieren, müssen wir den Datensatz in ein Trainingsset und ein Testset aufteilen. Wir werden die `train_test_split`-Funktion aus der scikit-learn-Bibliothek verwenden, um dies zu tun.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
