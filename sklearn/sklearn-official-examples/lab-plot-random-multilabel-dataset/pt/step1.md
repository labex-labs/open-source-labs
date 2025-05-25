# Importar Bibliotecas Necessárias e Definir Constantes

Primeiro, precisamos importar as bibliotecas necessárias e definir as cores e a constante de semente aleatória para gerar o conjunto de dados multirótulo.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # vermelho
        "#0198E1",  # azul
        "#BF5FFF",  # roxo
        "#FCD116",  # amarelo
        "#FF7216",  # laranja
        "#4DBD33",  # verde
        "#87421F",  # marrom
    ]
)

# Utilize a mesma semente aleatória para múltiplas chamadas a make_multilabel_classification para garantir as mesmas distribuições
RANDOM_SEED = np.random.randint(2**10)
```
