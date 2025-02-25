# Agregar etiquetas y ajustar el diseño

Agrega un título y etiquetas de eje a los subgráficos utilizando las funciones title, xlabel e ylabel de matplotlib.pyplot. Ajusta el diseño de los subgráficos utilizando la función tight_layout.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
