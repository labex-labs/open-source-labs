# Ejes gemelos con aspecto cuadrado

Vamos a crear un eje cuadrado, con un eje gemelo. El eje gemelo adopta el aspecto del contenedor del padre.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```
