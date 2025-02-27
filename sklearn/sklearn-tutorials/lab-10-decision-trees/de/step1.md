# Importieren der erforderlichen Bibliotheken

Zunächst müssen wir die erforderlichen Bibliotheken importieren. Wir werden scikit-learn verwenden, um den Entscheidungsbaum-Klassifizierer zu erstellen und zu trainieren.

```python
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```