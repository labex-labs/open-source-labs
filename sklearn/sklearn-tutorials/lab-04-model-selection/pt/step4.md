# Estimadores Validados Cruzadamente

Alguns estimadores no scikit-learn possuem capacidades de validação cruzada incorporadas. Estes estimadores validados cruzadamente selecionam automaticamente seus parâmetros por meio de validação cruzada, tornando o processo de seleção do modelo mais eficiente.

```python
from sklearn import linear_model, datasets

# Cria um objeto LassoCV
lasso = linear_model.LassoCV()

# Carrega o conjunto de dados de diabetes
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)

# Ajusta o objeto LassoCV no conjunto de dados
lasso.fit(X_diabetes, y_diabetes)

print(lasso.alpha_)
```
