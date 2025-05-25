# Construindo Arrays de Inteiros Anuláveis

O Pandas fornece a classe `IntegerArray` para criar arrays de inteiros anuláveis. Vamos começar criando um `IntegerArray`.

```python
# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np

# Criar um IntegerArray com valores ausentes
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```

Você também pode usar o alias de string "Int64" para especificar o tipo de dado ao criar o array. Todos os valores semelhantes a NA são substituídos por `pandas.NA`.

```python
# Criar um IntegerArray usando o alias de string "Int64"
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Output: <IntegerArray>
# [1, 2, <NA>]
# Length: 3, dtype: Int64
```
