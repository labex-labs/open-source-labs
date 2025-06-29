# Agregar una caja de texto con estadísticas

Ahora que tenemos un histograma básico, mejorémoslo agregando una caja de texto que muestre la información estadística sobre nuestros datos. Esto hará que la visualización sea más informativa para los espectadores.

## Creación del contenido de texto

Primero, necesitamos preparar el contenido de texto que irá dentro de nuestra caja de texto. En una nueva celda, ingrese y ejecute el siguiente código:

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

Debería ver una salida similar a la siguiente:

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

Este código crea una cadena de varias líneas que contiene la media, la mediana y la desviación estándar de nuestros datos. Analicemos algunos aspectos interesantes de este código:

1. El método `\n'.join(...)` une múltiples cadenas con un carácter de nueva línea entre ellas.
2. La `r` antes de cada cadena la convierte en una cadena "cruda", lo cual es útil cuando se incluyen caracteres especiales.
3. La notación `$...$` se utiliza para el formato matemático en estilo LaTeX en matplotlib.
4. `\mu` y `\sigma` son símbolos de LaTeX para las letras griegas μ (mu) y σ (sigma).
5. `%.2f` es un especificador de formato que muestra un número de punto flotante con dos decimales.

## Creación y adición de la caja de texto

Ahora, recreemos nuestro histograma y agreguemos la caja de texto a él. En una nueva celda, ingrese y ejecute el siguiente código:

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

Cuando ejecute esta celda, debería ver su histograma con una caja de texto en la esquina superior izquierda que muestra las estadísticas.

## Comprensión del código de la caja de texto

Analicemos las partes importantes del código que crea la caja de texto:

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:
   - Esto crea un diccionario con propiedades para la caja de texto.
   - `boxstyle='round'`: Hace que la caja tenga esquinas redondeadas.
   - `facecolor='wheat'`: Establece el color de fondo de la caja en color trigo.
   - `alpha=0.5`: Hace que la caja sea semi-transparente (50% de opacidad).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - Esto agrega texto a los ejes en la posición (0.05, 0.95).
   - `transform=ax.transAxes`: Esto es crucial, significa que las coordenadas están en unidades de ejes (0 - 1) en lugar de unidades de datos. Entonces, (0.05, 0.95) significa "5% desde el borde izquierdo y 95% desde el borde inferior del gráfico".
   - `fontsize=14`: Establece el tamaño de la fuente.
   - `verticalalignment='top'`: Alinea el texto de modo que la parte superior del texto esté en la coordenada y especificada.
   - `bbox=properties`: Aplica nuestras propiedades de la caja de texto.

La caja de texto permanecerá en la misma posición en relación con los ejes del gráfico, incluso si se hace zoom en el gráfico o se cambia el rango de datos. Esto se debe a que usamos `transform=ax.transAxes`, que utiliza coordenadas de ejes en lugar de coordenadas de datos.
