# Carregar Dados

Neste passo, carregaremos o conjunto de dados iris utilizando o módulo datasets do scikit-learn. Selecionaremos as duas primeiras características do conjunto de dados e atribuiremos-nas à variável X. Também atribuiremos a variável alvo a Y.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
