# Adicionar Anotação

Podemos adicionar uma anotação ao gráfico polar especificando a localização da anotação. Neste caso, escolhemos um ponto específico no gráfico e o anotamos.

```python
ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
```
