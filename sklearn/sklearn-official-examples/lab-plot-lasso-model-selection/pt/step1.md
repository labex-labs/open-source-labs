# Conjunto de Dados

Primeiro, carregaremos o conjunto de dados de diabetes usando a função `load_diabetes` de `sklearn.datasets`. O conjunto de dados consiste em 10 variáveis ​​de base, idade, sexo, índice de massa corporal, pressão arterial média e seis medições de soro sanguíneo, e uma medida quantitativa da progressão da doença um ano após a linha de base.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
