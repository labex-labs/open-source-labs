# Ajustar o Alinhamento dos Rótulos de Marcação (Tick Label)

Finalmente, podemos usar os métodos `set_ha` e `set_va` para ajustar o alinhamento horizontal e vertical dos rótulos de marcação (tick labels).

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
