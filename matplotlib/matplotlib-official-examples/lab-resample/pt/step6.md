# Criando o gráfico

Criaremos um gráfico usando Matplotlib. Criaremos uma instância `d` da classe `DataDisplayDownsampler` usando `xdata` e `ydata`. Criaremos uma figura e um eixo usando a função `subplots`. Conectaremos a linha e definiremos `autoscale` como `False`. Conectaremos para mudar os limites de visualização, definiremos o limite x e mostraremos o gráfico.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
