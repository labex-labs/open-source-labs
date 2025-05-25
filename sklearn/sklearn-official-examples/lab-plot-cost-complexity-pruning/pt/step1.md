# Carregar os Dados

Utilizaremos o conjunto de dados de cancro da mama do scikit-learn. Este conjunto de dados possui 30 características e uma variável alvo binária que indica se um paciente tem cancro maligno ou benigno.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
