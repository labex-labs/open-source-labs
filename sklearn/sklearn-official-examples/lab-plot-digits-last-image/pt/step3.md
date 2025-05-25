# Preparando o Conjunto de Dados para Aprendizado de Máquina

Antes de treinar um modelo de aprendizado de máquina no conjunto de dados, precisamos prepará-lo dividindo-o em conjuntos de treinamento e teste. Podemos fazer isso usando a função `train_test_split` do scikit-learn:

```python
from sklearn.model_selection import train_test_split

# Dividir o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
