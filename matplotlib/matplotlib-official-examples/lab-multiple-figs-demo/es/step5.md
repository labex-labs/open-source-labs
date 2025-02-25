# Hacer cambios en la figura 1

Ahora, volveremos a la primera figura y haremos algunos cambios. Graficaremos la segunda onda senoidal en el subgráfico superior usando marcadores cuadrados y eliminaremos las etiquetas de las marcas del eje x del subgráfico superior.

```python
plt.figure(1)

# Subgráfico superior
plt.subplot(211)
plt.plot(t, s2,'s')
ax = plt.gca()
ax.set_xticklabels([])
```
