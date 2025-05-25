# Criar o gráfico de barras horizontais quebradas

Nesta etapa, criaremos o gráfico de barras horizontais quebradas. Usaremos o método `broken_barh()` da classe `Axes` para criar o gráfico. O método `broken_barh()` recebe três argumentos: o primeiro argumento é uma lista de tuplas, onde cada tupla representa um segmento da barra e o primeiro elemento da tupla é o ponto de partida do segmento e o segundo elemento é o comprimento do segmento; o segundo argumento é a coordenada y da barra; e o terceiro argumento é a cor de preenchimento (face color) da barra.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
