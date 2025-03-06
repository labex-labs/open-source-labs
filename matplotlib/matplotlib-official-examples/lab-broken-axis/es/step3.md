# Añadiendo toques finales al gráfico con eje roto

En este último paso, añadiremos toques finales a nuestro gráfico con eje roto para dejar claro que el eje y está roto. Añadiremos líneas diagonales entre los subgráficos para indicar la ruptura y mejoraremos la apariencia general del gráfico con etiquetas adecuadas y una cuadrícula.

## Añadir líneas diagonales de ruptura

Para indicar visualmente que el eje está roto, añadiremos líneas diagonales entre los dos subgráficos. Esta es una convención común que ayuda a los espectadores a entender que se ha omitido una parte del eje.

Crea una nueva celda y añade el siguiente código:

```python
# Crea dos subgráficos apilados verticalmente con eje x compartido
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Grafica los mismos datos en ambos ejes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Establece los límites del eje y para cada subgráfico
ax1.set_ylim(0.78, 1.0)    # El subgráfico superior muestra solo los valores atípicos
ax2.set_ylim(0, 0.22)      # El subgráfico inferior muestra solo los datos principales

# Oculta las líneas de los ejes entre ax1 y ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Ajusta la posición de las marcas
ax1.xaxis.tick_top()          # Mueve las marcas del eje x hacia la parte superior
ax1.tick_params(labeltop=False)  # Oculta las etiquetas de las marcas del eje x en la parte superior
ax2.xaxis.tick_bottom()       # Mantiene las marcas del eje x en la parte inferior

# Añade líneas diagonales de ruptura
d = 0.5  # proporción de la extensión vertical a horizontal de la línea inclinada
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Añade etiquetas y un título
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Añade una cuadrícula a ambos subgráficos para mayor legibilidad
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Ajusta el espacio entre subgráficos
plt.show()
```

Cuando ejecutes esta celda, deberías ver el gráfico con eje roto completo con líneas diagonales que indican la ruptura en el eje y. El gráfico ahora tiene un título, etiquetas de ejes y líneas de cuadrícula para mejorar la legibilidad.

## Entendiendo el gráfico con eje roto

Tomemos un momento para entender los componentes clave de nuestro gráfico con eje roto:

1. **Dos subgráficos**: Creamos dos subgráficos separados, cada uno centrado en un rango diferente de valores en el eje y.
2. **Líneas de los ejes ocultas**: Ocultamos las líneas de los ejes que conectan los subgráficos para crear una separación visual.
3. **Líneas diagonales de ruptura**: Añadimos líneas diagonales para indicar que el eje está roto.
4. **Límites del eje y**: Establecimos diferentes límites para el eje y en cada subgráfico para centrarnos en partes específicas de los datos.
5. **Líneas de cuadrícula**: Añadimos líneas de cuadrícula para mejorar la legibilidad y facilitar la estimación de valores.

Esta técnica es especialmente útil cuando tienes valores atípicos en tus datos que de otro modo comprimirían la visualización de la mayoría de tus puntos de datos. Al "romper" el eje, puedes mostrar tanto los valores atípicos como la distribución principal de los datos de manera clara en una sola figura.

## Experimentar con el gráfico

Ahora que entiendes cómo crear un gráfico con eje roto, puedes experimentar con diferentes configuraciones. Intenta cambiar los límites del eje y, añadir más características al gráfico o aplicar esta técnica a tus propios datos.

Por ejemplo, puedes modificar el código anterior para incluir una leyenda, cambiar el esquema de colores o ajustar los estilos de los marcadores:

```python
# Crea dos subgráficos apilados verticalmente con eje x compartido
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Grafica los mismos datos en ambos ejes con diferentes estilos
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Marca los valores atípicos con un color diferente
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Establece los límites del eje y para cada subgráfico
ax1.set_ylim(0.78, 1.0)    # El subgráfico superior muestra solo los valores atípicos
ax2.set_ylim(0, 0.22)      # El subgráfico inferior muestra solo los datos principales

# Oculta las líneas de los ejes entre ax1 y ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Ajusta la posición de las marcas
ax1.xaxis.tick_top()          # Mueve las marcas del eje x hacia la parte superior
ax1.tick_params(labeltop=False)  # Oculta las etiquetas de las marcas del eje x en la parte superior
ax2.xaxis.tick_bottom()       # Mantiene las marcas del eje x en la parte inferior

# Añade líneas diagonales de ruptura
d = 0.5  # proporción de la extensión vertical a horizontal de la línea inclinada
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Añade etiquetas y un título
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Añade una cuadrícula a ambos subgráficos para mayor legibilidad
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Añade una leyenda al subgráfico
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Ajusta el espacio entre subgráficos
plt.show()
```

Cuando ejecutes este código mejorado, deberías ver una visualización mejorada con los valores atípicos marcados y una leyenda que explica los puntos de datos.

¡Felicidades! Has creado con éxito un gráfico con eje roto en Python utilizando Matplotlib. Esta técnica te ayudará a crear visualizaciones más efectivas cuando trabajes con datos que contengan valores atípicos.
