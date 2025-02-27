# Metrikfunktionen

Das scikit-learn-`metrics`-Modul implementiert mehrere Funktionen zur Beurteilung der Vorhersagefehler für spezifische Zwecke. Diese Funktionen können verwendet werden, um die Qualität der Vorhersagen eines Modells zu berechnen.

Hier ist ein Beispiel für die Verwendung der `accuracy_score`-Funktion aus dem `metrics`-Modul:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
