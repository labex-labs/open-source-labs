# Criar o Objeto RFE e Ajustar os Dados

Em seguida, criaremos um objeto da classe RFE e ajustaremos os dados a ele. Usaremos um Classificador de Vetores de Suporte (SVC) com um kernel linear como o estimador. Selecionaremos uma característica de cada vez e daremos um passo de cada vez.

```python
from sklearn.svm import SVC
from sklearn.feature_selection import RFE

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
```
