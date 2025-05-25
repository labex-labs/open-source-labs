# Importar Matplotlib e criar um gráfico de dispersão

Começamos importando o Matplotlib e criando um gráfico de dispersão.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
