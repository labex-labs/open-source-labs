# Creación de una visualización final con múltiples elementos de texto

En este último paso, combinaremos todo lo que hemos aprendido para crear una visualización integral que incluya múltiples elementos de texto con diferentes estilos. Esto demostrará cómo se pueden utilizar las cajas de texto para mejorar la narración de datos.

## Creación de una visualización avanzada

Creemos un gráfico más sofisticado que incluya tanto nuestro histograma como algunos elementos visuales adicionales. En una nueva celda, ingrese y ejecute el siguiente código:

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

Cuando ejecute esta celda, verá una visualización integral con:

- Un histograma de los datos con un estilo mejorado.
- Líneas verticales que marcan la media y el rango de una desviación estándar.
- Una caja de texto con estadísticas en la esquina superior izquierda.
- Una caja de texto informativa sobre distribuciones normales en la esquina superior derecha.
- Una leyenda que explica las líneas verticales.

## Comprensión de los elementos avanzados

Examinemos algunos de los nuevos elementos que hemos agregado:

1. **Líneas verticales con `axvline()`**:

   - Estas líneas marcan estadísticas importantes directamente en el gráfico.
   - El parámetro `label` permite que estas líneas se incluyan en la leyenda.

2. **Múltiples cajas de texto con diferentes estilos**:

   - Cada caja de texto tiene un propósito diferente y utiliza un estilo distinto.
   - La caja de estadísticas muestra los valores calculados a partir de nuestros datos.
   - La caja informativa proporciona contexto sobre las distribuciones normales.

3. **Formato mejorado**:

   - Se utiliza el formato LaTeX para crear texto en negrita con `\mathbf{}`.
   - Se crean viñetas con `\bullet`.
   - El espaciado se controla con `\ ` (barra invertida seguida de un espacio).

4. **Cuadrícula y leyenda**:
   - La cuadrícula ayuda a los espectadores a leer los valores del gráfico con mayor precisión.
   - La leyenda explica el significado de las líneas de color.

## Notas finales sobre la colocación de cajas de texto

Al colocar múltiples elementos de texto en una visualización, considere:

1. **Jerarquía visual**: La información más importante debe destacarse más.
2. **Posicionamiento**: Coloque la información relacionada cerca de las partes relevantes de la visualización.
3. **Contraste**: Asegúrese de que el texto sea legible sobre su fondo.
4. **Consistencia**: Utilice un estilo consistente para tipos de información similares.
5. **Desorden**: Evite abarrotar la visualización con demasiados elementos de texto.

Al colocar y dar estilo a las cajas de texto de manera reflexiva, puede crear visualizaciones que sean informativas y visualmente atractivas, guiando a los espectadores para que comprendan los principales insights de sus datos.
