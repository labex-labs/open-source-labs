# Mostrar o eixo y direito do primeiro eixo parasita

Mostramos o eixo y direito do primeiro eixo parasita usando o método `par1.axis["right"].set_visible(True)`. Também definimos `par1.axis["right"].major_ticklabels.set_visible(True)` e `par1.axis["right"].label.set_visible(True)` para mostrar os rótulos de marcação (tick labels) e o rótulo do eixo y direito.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```
