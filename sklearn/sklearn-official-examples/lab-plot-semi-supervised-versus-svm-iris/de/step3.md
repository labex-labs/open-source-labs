# Einrichten der Self-training-Klassifizierer

Wir werden zwei Self-training-Klassifizierer mit unterschiedlichen Prozentsätzen markierter Daten einrichten: 30% und 50%. Self-training ist ein halbüberwachtes Lernverfahren, das einen Klassifizierer auf den markierten Daten trainiert und dann verwendet, um die Labels der unmarkierten Daten vorherzusagen. Die am zuverlässigsten vorhergesagten Labels werden zu den markierten Daten hinzugefügt, und der Prozess wird wiederholt, bis die Konvergenz erreicht ist.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Einrichten der Self-training-Klassifizierer
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% Daten",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% Daten",
)
```
