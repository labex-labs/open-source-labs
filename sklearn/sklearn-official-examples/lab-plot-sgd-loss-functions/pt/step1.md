# Importar Bibliotecas e Definir Funções

Começamos importando as bibliotecas necessárias e definindo a função de perda Huber modificada.

```python
import numpy as np
import matplotlib.pyplot as plt

def modified_huber_loss(y_true, y_pred):
    z = y_pred * y_true
    loss = -4 * z
    loss[z >= -1] = (1 - z[z >= -1]) ** 2
    loss[z >= 1.0] = 0
    return loss
```
