# Ajustar la alineación de las etiquetas de las marcas

Finalmente, podemos usar los métodos `set_ha` y `set_va` para ajustar la alineación horizontal y vertical de las etiquetas de las marcas.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```
