# Remoção de características com baixa variância

A classe `VarianceThreshold` no scikit-learn pode ser usada para remover características com baixa variância. Características com baixa variância geralmente não fornecem muita informação para o modelo. Vamos demonstrar como usar `VarianceThreshold` para remover características com variância zero.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Inicializa VarianceThreshold com um limiar de 80% de variabilidade
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

# Seleciona características com alta variabilidade
X_selected = sel.fit_transform(X)

print("Forma original de X:", X.shape)
print("Forma de X com características selecionadas:", X_selected.shape)
print("Características selecionadas:", sel.get_support(indices=True))
```

Este fragmento de código demonstra como usar `VarianceThreshold` para remover características com variância zero de um conjunto de dados. A saída mostrará a forma original do conjunto de dados e a forma após a seleção de características com alta variabilidade.
