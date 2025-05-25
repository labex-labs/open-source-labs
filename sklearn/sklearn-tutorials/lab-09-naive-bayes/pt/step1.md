# Importar Bibliotecas e Carregar o Conjunto de Dados

Comecemos importando as bibliotecas necessárias e carregando o conjunto de dados iris. Usaremos a função `load_iris` do módulo `sklearn.datasets` para carregar o conjunto de dados.

```python
from sklearn.datasets import load_iris

# Carregar o conjunto de dados iris
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Variável alvo

print("Número de amostras:", X.shape[0])
print("Número de características:", X.shape[1])
print("Número de classes:", len(set(y)))
```
