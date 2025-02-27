# Daten laden und Modell trainieren

Für dieses Beispiel verwenden wir einen Datensatz von einem Bluttransfusionsdienstzentrum aus OpenML. Das Ziel ist, zu bestimmen, ob eine Person Blut gespendet hat. Zunächst wird der Datensatz in Trainings- und Testdaten aufgeteilt, und anschließend wird ein logistisches Regressionsmodell mit dem Trainingsdatensatz trainiert.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```
