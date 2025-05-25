# Definir os Limites-x Usando Escalares ou Unidades

Nesta etapa, definiremos os limites-x usando escalares ou unidades. Usaremos o método `set_xlim` para definir os limites-x. Definiremos os limites-x para 2 e 6 usando escalares nas unidades atuais para o gráfico de barras na segunda linha e primeira coluna. Definiremos os limites-x para 2 cm e 6 cm usando unidades para o gráfico de barras na segunda linha e segunda coluna.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
