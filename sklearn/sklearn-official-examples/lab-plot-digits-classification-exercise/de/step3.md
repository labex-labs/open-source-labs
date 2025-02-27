# Teilen Sie den Datensatz in Trainings- und Testsets auf

Als nächstes werden wir den Datensatz mit der Funktion `train_test_split` von scikit-learn in Trainings- und Testsets aufteilen. Wir werden 90% der Daten für das Training und 10% für das Testen verwenden.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
