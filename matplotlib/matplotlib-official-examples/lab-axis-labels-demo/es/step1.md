# Importar Matplotlib y crear un diagrama de dispersión

Comenzamos importando Matplotlib y creando un diagrama de dispersión.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
