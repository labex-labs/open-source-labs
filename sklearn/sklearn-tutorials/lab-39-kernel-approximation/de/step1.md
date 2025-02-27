# Nystroem-Methode zur Kernel-Approximation

Die Nystroem-Methode ist eine allgemeine Technik zur Approximation von Kernen unter Verwendung einer niedergradigen Approximation. Sie entnimmt einer Stichprobe des Datensatzes, auf dem der Kernel ausgewertet wird. Standardmäßig verwendet sie den RBF-Kernel, kann aber mit jeder Kernel-Funktion oder einer vorgegebenen Kernel-Matrix verwendet werden.

Um die Nystroem-Methode zur Kernel-Approximation zu verwenden, führen Sie die folgenden Schritte aus:

1. Initialisieren Sie das Nystroem-Objekt mit der gewünschten Anzahl von Komponenten (d.h., der Ziel-Dimensionalität der Merkmalstransformation).

```python
from sklearn.kernel_approximation import Nystroem

n_components = 100
nystroem = Nystroem(n_components=n_components)
```

2. Passen Sie das Nystroem-Objekt an Ihre Trainingsdaten an.

```python
nystroem.fit(X_train)
```

3. Transformieren Sie Ihre Trainings- und Testdaten mit dem Nystroem-Objekt.

```python
X_train_transformed = nystroem.transform(X_train)
X_test_transformed = nystroem.transform(X_test)
```
