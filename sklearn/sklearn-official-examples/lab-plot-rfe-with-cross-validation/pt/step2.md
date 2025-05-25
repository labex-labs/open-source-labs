# Treinamento e Seleção do Modelo

Criaremos o objeto RFECV e calculamos as pontuações validadas cruzadamente. A estratégia de pontuação "accuracy" otimiza a proporção de amostras classificadas corretamente. Usaremos regressão logística como estimador e validação cruzada estratificada k-fold com 5 dobras.

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # Número mínimo de recursos a considerar
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Número ótimo de recursos: {rfecv.n_features_}")
```
