# Definir a Estrutura dos Dados

Os pixels numa imagem estão conectados aos seus vizinhos. Para realizar o agrupamento hierárquico numa imagem, precisamos definir a estrutura dos dados. Podemos usar a função `grid_to_graph` do scikit-learn para criar uma matriz de conectividade que define a estrutura dos dados.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
