# Importar Matplotlib y crear una figura y un eje

Primero, debe importar Matplotlib y crear una figura y un eje. La figura y el eje son los contenedores de su gráfico.

```python
import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
