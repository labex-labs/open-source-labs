# Agregar una leyenda al diagrama

Ahora agregaremos una leyenda al diagrama. Hay dos maneras de agregar una leyenda en Matplotlib. Usaremos ambos métodos en este ejemplo.

```python
# Método 1: Colocar una leyenda encima del subdiagrama
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Método 2: Colocar una leyenda a la derecha del subdiagrama
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
