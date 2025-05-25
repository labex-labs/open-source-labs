# Formatar o gráfico

Para tornar nosso gráfico mais legível, podemos formatá-lo usando as funções de formatação do Matplotlib. Neste exemplo, formataremos os rótulos do eixo y para exibir valores em milhões.

```python
def millions(x):
    return '$%1.1fM' % (x * 1e-6)

ax.fmt_ydata = millions
```
