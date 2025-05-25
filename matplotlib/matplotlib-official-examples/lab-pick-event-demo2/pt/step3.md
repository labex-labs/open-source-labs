# Plotar os Dados

Agora, plotaremos mu vs. sigma usando o módulo `pyplot` do Matplotlib. Criaremos um gráfico de dispersão (scatter plot) usando os valores calculados para mu e sigma. Também adicionaremos interatividade ao gráfico definindo o parâmetro `picker` como True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
