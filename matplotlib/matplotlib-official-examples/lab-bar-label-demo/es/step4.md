# Etiquetado avanzado de barras

En este paso, mostraremos algunas cosas más avanzadas que se pueden hacer con las etiquetas de barras. Usaremos el mismo diagrama de barras horizontal que en el paso anterior.

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # etiquetas leídas de arriba hacia abajo
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Etiquetar con leyendas dadas, relleno personalizado y opciones de anotación
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```
