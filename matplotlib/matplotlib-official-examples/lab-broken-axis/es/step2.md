# Creando y configurando el gráfico con eje roto

En este paso, crearemos la estructura real del gráfico con eje roto. Un gráfico con eje roto consiste en múltiples subgráficos que muestran diferentes rangos de los mismos datos. Configuraremos estos subgráficos para mostrar eficazmente nuestros datos principales y valores atípicos (outliers).

## Crear los subgráficos

Primero, necesitamos crear dos subgráficos dispuestos verticalmente. El subgráfico superior mostrará nuestros valores atípicos, mientras que el subgráfico inferior mostrará la mayoría de nuestros puntos de datos.

Crea una nueva celda en tu cuaderno (notebook) y agrega el siguiente código:

```python
# Crea dos subgráficos apilados verticalmente con eje x compartido
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Agrega un título principal a la figura
fig.suptitle('Broken Axis Plot Example', fontsize=16)

# Grafica los mismos datos en ambos ejes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Muestra la figura para ver ambos subgráficos
plt.tight_layout()
plt.show()
```

![broken-axis-plot](../assets/screenshot-20250306-cawcMZv3@2x.png)

Cuando ejecutes esta celda, deberías ver una figura con dos subgráficos, ambos mostrando los mismos datos. Observa cómo los valores atípicos comprimen el resto de los datos en ambos gráficos, lo que dificulta ver los detalles de la mayoría de los puntos de datos. Este es exactamente el problema que intentamos resolver con un gráfico con eje roto.

## Configurar los límites del eje Y

Ahora necesitamos configurar cada subgráfico para centrarse en un rango específico de valores en el eje y. El subgráfico superior se centrará en el rango de valores atípicos, mientras que el subgráfico inferior se centrará en el rango de los datos principales.

Crea una nueva celda y agrega el siguiente código:

```python
# Crea dos subgráficos apilados verticalmente con eje x compartido
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Grafica los mismos datos en ambos ejes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Establece los límites del eje y para cada subgráfico
ax1.set_ylim(0.78, 1.0)    # El subgráfico superior muestra solo los valores atípicos
ax2.set_ylim(0, 0.22)      # El subgráfico inferior muestra solo los datos principales

# Agrega un título a cada subgráfico
ax1.set_title('Outlier Region')
ax2.set_title('Main Data Region')

# Muestra la figura con los límites del eje y ajustados
plt.tight_layout()
plt.show()
```

Cuando ejecutes esta celda, deberías ver que cada subgráfico ahora se centra en un rango diferente de valores en el eje y. El gráfico superior muestra solo los valores atípicos, y el gráfico inferior muestra solo los datos principales. Esto ya mejora la visualización, pero para convertirlo en un gráfico con eje roto adecuado, necesitamos agregar algunas configuraciones más.

## Ocultar las líneas de los ejes (spines) y ajustar las marcas (ticks)

Para crear la ilusión de un eje "roto", necesitamos ocultar las líneas de los ejes que conectan los dos subgráficos y ajustar la posición de las marcas.

Crea una nueva celda y agrega el siguiente código:

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

# Agrega etiquetas al gráfico
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')

plt.tight_layout()
plt.show()
```

Cuando ejecutes esta celda, deberías ver que el gráfico ahora tiene las líneas de los ejes ocultas entre los dos subgráficos, lo que crea una apariencia más limpia. Las marcas del eje x ahora están posicionadas correctamente, con etiquetas solo en la parte inferior.

En este punto, hemos creado con éxito un gráfico con eje roto básico. En el siguiente paso, agregaremos toques finales para que quede claro para los espectadores que el eje está roto.
