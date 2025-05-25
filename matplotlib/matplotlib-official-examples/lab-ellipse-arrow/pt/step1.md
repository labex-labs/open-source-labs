# Importar Matplotlib e Criar uma Figura e Eixo

Primeiramente, você precisa importar Matplotlib e criar uma figura e um eixo. A figura e o eixo são os contêineres para o seu gráfico.

```python
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
