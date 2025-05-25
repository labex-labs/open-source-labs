# Compreendendo Conjuntos de Dados

O scikit-learn representa conjuntos de dados como matrizes 2D, onde o primeiro eixo representa as amostras e o segundo eixo representa as características. Vamos dar uma olhada em um exemplo usando o conjunto de dados iris:

```python
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
print(data.shape)
```

Saída:

```
(150, 4)
```

O conjunto de dados iris consiste em 150 observações de íris, com cada observação descrita por 4 características. A forma da matriz de dados é (150, 4).
