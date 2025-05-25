# Ajustamento e Calibração

Treinamos um classificador de floresta aleatória com 25 estimadores base (árvores) nos dados de treino e validação concatenados (1000 amostras). Este é o classificador não calibrado.

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

Para treinar o classificador calibrado, começamos com o mesmo classificador de floresta aleatória, mas treinamo-lo apenas com o subconjunto de dados de treino (600 amostras), e em seguida calibramos, com `method='sigmoid'`, utilizando o subconjunto de dados de validação (400 amostras) num processo em duas etapas.

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
