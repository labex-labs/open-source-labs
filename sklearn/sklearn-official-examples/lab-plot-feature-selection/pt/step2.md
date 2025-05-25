# Seleção de Características Univariada

Em seguida, realizaremos a seleção de características univariada com o teste F para pontuação das características. Usaremos a função de seleção padrão para selecionar as quatro características mais significativas.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
