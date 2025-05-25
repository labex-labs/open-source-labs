# Encolhimento de Ledoit-Wolf

O método de encolhimento de Ledoit-Wolf fornece um coeficiente de encolhimento ótimo que minimiza o erro quadrático médio entre a matriz de covariância estimada e a verdadeira. O pacote `sklearn.covariance` inclui uma função `ledoit_wolf` que pode ser usada para calcular o estimador de Ledoit-Wolf para um conjunto de dados dado.

```python
from sklearn.covariance import ledoit_wolf

# Calcular o estimador de Ledoit-Wolf da matriz de covariância
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
