# Beispiel-Daten generieren

Zunächst werden wir einige Beispiel-Daten für die Demonstration generieren. Wir werden den Iris-Datensatz verwenden und diesem einige nicht korrelierende rauschende Daten hinzufügen.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Der Iris-Datensatz
X, y = load_iris(return_X_y=True)

# Einige rauschende Daten, die nicht korreliert sind
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Fügen Sie die rauschenden Daten zu den informativen Merkmalen hinzu
X = np.hstack((X, E))

# Teilen Sie den Datensatz in Trainings- und Testdaten auf, um die Feature-Selektion durchzuführen und den Klassifikator zu evaluieren
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
