# Gerar Dados de Amostra

Primeiro, geraremos alguns dados de amostra para a demonstração. Usaremos o conjunto de dados iris e adicionaremos alguns dados ruidosos não correlacionados a ele.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# O conjunto de dados iris
X, y = load_iris(return_X_y=True)

# Alguns dados ruidosos não correlacionados
E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))

# Adiciona os dados ruidosos às características informativas
X = np.hstack((X, E))

# Divide o conjunto de dados para selecionar a característica e avaliar o classificador
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
```
