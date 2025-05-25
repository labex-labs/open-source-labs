# Importar Matplotlib

Antes de começarmos a anotar gráficos com Matplotlib, devemos primeiro importar a biblioteca. Nesta etapa, importaremos Matplotlib e criaremos um gráfico simples para usar na anotação.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```
