# Carregar o conjunto de dados

Primeiro, precisamos carregar um conjunto de dados que podemos usar para treinar nosso modelo preditivo. Usaremos o conjunto de dados Diabetes do scikit-learn, que contém informações sobre pacientes com diabetes.

```python
from sklearn.datasets import load_diabetes

# Carregar o conjunto de dados Diabetes
diabetes = load_diabetes()

# Dividir os dados em conjuntos de treinamento e validação
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
