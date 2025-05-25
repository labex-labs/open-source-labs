# Seleção de características univariada

A seleção de características univariada funciona selecionando as melhores características com base em testes estatísticos univariados. No scikit-learn, existem várias classes que implementam a seleção de características univariada:

- `SelectKBest`: seleciona as k características com as pontuações mais altas.
- `SelectPercentile`: seleciona uma porcentagem especificada pelo usuário das características com as pontuações mais altas.
- `SelectFpr`: seleciona características com base na taxa de falsos positivos.
- `SelectFdr`: seleciona características com base na taxa de falsos descobrimentos.
- `SelectFwe`: seleciona características com base no erro do tipo I familiar.
- `GenericUnivariateSelect`: permite a seleção com uma estratégia configurável.

Aqui está um exemplo de uso de `SelectKBest` para selecionar as duas melhores características do conjunto de dados Iris:

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Carrega o conjunto de dados Iris
X, y = load_iris(return_X_y=True)

# Inicializa SelectKBest com a função de pontuação f_classif e k=2
selector = SelectKBest(f_classif, k=2)

# Seleciona as melhores características
X_selected = selector.fit_transform(X, y)

print("Forma original de X:", X.shape)
print("Forma de X com características selecionadas:", X_selected.shape)
print("Características selecionadas:", selector.get_support(indices=True))
```

Neste exemplo, usamos a função de pontuação `f_classif` e selecionamos as duas melhores características do conjunto de dados Iris. A saída mostrará a forma original do conjunto de dados e a forma após a seleção das melhores características.
