# Charger les données et entraîner le modèle

Pour cet exemple, nous utiliserons un ensemble de données de centre de services de transfusion sanguine provenant d'OpenML. La variable cible est de savoir si une personne a fait un don de sang. Tout d'abord, les données sont divisées en ensembles d'entraînement et de test, puis un modèle de régression logistique est ajusté avec l'ensemble d'entraînement.

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
