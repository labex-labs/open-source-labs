# Seleção de Características usando SelectFromModel

A classe `SelectFromModel` é um meta-transformador que pode ser usado com qualquer estimador que atribua importância a cada característica. Seleciona características com base em sua importância e remove características abaixo de um limiar especificado.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Carrega o conjunto de dados Iris
X, y = load_iris(return_X_y=True)

# Inicializa RandomForestClassifier como o estimador
estimator = RandomForestClassifier()

# Inicializa SelectFromModel com o estimador e limiar de "média"
selector = SelectFromModel(estimator, threshold="mean")

# Seleciona as melhores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X com características selecionadas:", X_selected.shape)
print("Características selecionadas:", selector.get_support(indices=True))
```

Neste exemplo, usamos um Classificador Random Forest como o estimador e selecionamos características com uma importância maior que a média da importância. A saída mostrará a forma original do conjunto de dados e a forma após a seleção das melhores características.
