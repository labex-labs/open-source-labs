# Selecionando Características com Base na Importância

Selecionamos as duas características mais importantes de acordo com os coeficientes usando `SelectFromModel`. `SelectFromModel` aceita um parâmetro `threshold` e selecionará as características cuja importância (definida pelos coeficientes) estiver acima deste limiar.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Características selecionadas por SelectFromModel: {feature_names[sfm.get_support()]}")
```
