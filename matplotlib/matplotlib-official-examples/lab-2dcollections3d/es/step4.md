# Personalizar el gráfico

El cuarto paso es personalizar el gráfico agregando una leyenda, estableciendo los límites y etiquetas de los ejes y cambiando el ángulo de vista.

```python
# Hacer la leyenda, establecer los límites y etiquetas de los ejes
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Personalizar el ángulo de vista para que sea más fácil ver que los puntos de dispersión
# se encuentran en el plano y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()
```
