# Score und Kreuzvalidierte Scores

Schätzer in scikit-learn bieten eine `score`-Methode an, die verwendet werden kann, um die Qualität der Modellanpassung oder der Vorhersage für neue Daten zu bewerten. Diese Methode gibt einen Score zurück, wobei ein höherer Wert eine bessere Leistung anzeigt.

```python
from sklearn import datasets, svm

# Lade den Digits-Datensatz
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# Erstelle einen SVM-Klassifizierer mit linearer Kernel
svc = svm.SVC(C=1, kernel='linear')

# Trainiere den Klassifizierer auf den Trainingsdaten und berechne den Score auf den Testdaten
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

Um eine genauere Messung der Vorhersagegenauigkeit zu erhalten, können wir Kreuzvalidierung verwenden. Die Kreuzvalidierung besteht darin, die Daten in mehrere Folds aufzuteilen, wobei jeder Fold als Testmenge und die verbleibenden Folds als Trainingsmengen verwendet werden. Dieser Prozess wird mehrmals wiederholt, und die Scores werden gemittelt, um die Gesamtleistung zu erhalten.

```python
import numpy as np

# Teile die Daten in 3 Folds auf
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# Führe die Kreuzvalidierung durch
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
