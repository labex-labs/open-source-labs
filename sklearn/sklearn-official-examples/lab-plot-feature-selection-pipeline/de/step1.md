# Datensatz generieren und aufteilen

Wir beginnen mit der Generierung eines binären Klassifikationsdatensatzes mithilfe der `make_classification`-Funktion von Scikit-learn. Wir teilen den Datensatz auch in Trainings- und Testuntermengen auf, indem wir die `train_test_split`-Funktion von Scikit-learn verwenden.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
