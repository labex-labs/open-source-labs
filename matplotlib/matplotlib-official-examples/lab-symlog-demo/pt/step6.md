# Criar Gráfico Symlog nos eixos x e y

No terceiro subplot, criaremos um gráfico `symlog` tanto no eixo x quanto no eixo y. Também definiremos o parâmetro `linthresh` para 0.015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
