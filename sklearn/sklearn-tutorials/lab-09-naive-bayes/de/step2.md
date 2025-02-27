# Den Datensatz in Trainings- und Testsets unterteilen

Als nächstes werden wir den Datensatz unter Verwendung der Funktion `train_test_split` aus dem Modul `sklearn.model_selection` in Trainings- und Testsets aufteilen. Der Trainingssatz wird verwendet, um den Naiven Bayes-Klassifizierer zu trainieren, und der Testsatz wird verwendet, um seine Leistung zu evaluieren.

```python
from sklearn.model_selection import train_test_split

# Teilen Sie den Datensatz in Trainings- und Testsets auf
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
