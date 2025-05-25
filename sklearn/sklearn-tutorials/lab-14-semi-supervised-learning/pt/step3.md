# Propagação de Rótulos

#### Visão Geral do algoritmo de Propagação de Rótulos

A Propagação de Rótulos é um tipo de algoritmo semi-supervisionado de inferência de grafos. Constrói um grafo de similaridade sobre todos os itens no conjunto de dados de entrada e utiliza este grafo para propagar os rótulos dos dados rotulados para os dados não rotulados. A Propagação de Rótulos pode ser usada para tarefas de classificação e suporta métodos de kernel para projetar os dados em espaços dimensionais alternativos.

#### Utilizando a Propagação de Rótulos no scikit-learn

No scikit-learn, existem dois modelos de propagação de rótulos disponíveis: `LabelPropagation` e `LabelSpreading`. Ambos os modelos constroem um grafo de similaridade e propagam os rótulos. Aqui está um exemplo de como utilizar a Propagação de Rótulos:

```python
from sklearn.semi_supervised import LabelPropagation

# Crie um modelo de propagação de rótulos
propagacao_rotulos = LabelPropagation()

# Treine o modelo de propagação de rótulos nos dados rotulados
propagacao_rotulos.fit(X_labeled, y_labeled)

# Preveja os rótulos para novas amostras
y_pred = propagacao_rotulos.predict(X_test)
```

No exemplo acima, `X_labeled` e `y_labeled` são os dados rotulados, e `X_test` são as novas amostras a serem previstas.
