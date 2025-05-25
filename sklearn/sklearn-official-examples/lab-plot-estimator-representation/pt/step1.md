# Representação de Texto Compacta

A primeira forma de exibir estimadores é através da representação de texto compacta. Os estimadores apenas mostrarão os parâmetros que foram definidos com valores diferentes dos padrões quando exibidos como uma string. Isto reduz o ruído visual e facilita a identificação das diferenças ao comparar instâncias.

```python
from sklearn.linear_model import LogisticRegression

# Cria uma instância de Regressão Logística com penalidade l1
lr = LogisticRegression(penalty="l1")

# Exibe o estimador
print(lr)
```
