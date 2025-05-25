# Carregar Dados e Treinar o Modelo

Neste exemplo, usaremos um conjunto de dados de um centro de serviço de transfusão sanguínea do OpenML. A variável-alvo indica se um indivíduo doou sangue. Primeiro, os dados são divididos em conjuntos de treinamento e teste, e então um modelo de regressão logística é ajustado com o conjunto de dados de treinamento.

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
