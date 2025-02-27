# Definir los clasificadores

Definiremos varios solvers en línea para la clasificación, cada uno con diferentes hiperparámetros. Utilizaremos los siguientes clasificadores:

- SGDClassifier
- Perceptron
- PassiveAggressiveClassifier
- LogisticRegression

```python
from sklearn.linear_model import SGDClassifier, Perceptron, PassiveAggressiveClassifier, LogisticRegression

classifiers = [
    ("SGD", SGDClassifier(max_iter=1000)),
    ("Perceptron", Perceptron(max_iter=1000)),
    ("Passive-Aggressive I", PassiveAggressiveClassifier(max_iter=1000, loss="hinge", C=1.0, tol=1e-4)),
    ("Passive-Aggressive II", PassiveAggressiveClassifier(max_iter=1000, loss="squared_hinge", C=1.0, tol=1e-4)),
    ("LogisticRegression", LogisticRegression(max_iter=1000))
]
```
