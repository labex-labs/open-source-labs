# Training eines maschinellen Lernmodells

Jetzt, nachdem wir das Dataset vorbereitet haben, können wir ein maschinelles Lernmodell auf den Trainingsdaten trainieren. In diesem Beispiel werden wir einen Support Vector Machine (SVM)-Algorithmus verwenden:

```python
from sklearn.svm import SVC

# Erstellen Sie den SVM-Klassifizierer
clf = SVC(kernel='linear')

# Trainieren Sie den Klassifizierer auf den Trainingsdaten
clf.fit(X_train, y_train)
```
