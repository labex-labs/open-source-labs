# Formatear las Etiquetas del Eje Y con Signos de Dólar

Ahora, formateemos las etiquetas del eje y para mostrar signos de dólar. Utilizaremos la clase `StrMethodFormatter` del módulo `matplotlib.ticker` para formatear las etiquetas.

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

En el código anterior, creamos un objeto `StrMethodFormatter` con la cadena de formato `'$ {x:,.2f}'`. Esta cadena de formato especifica que queremos un signo de dólar seguido de un espacio, seguido de un número separado por comas con dos decimales.

A continuación, creamos un objeto `Tick` utilizando el objeto `StrMethodFormatter` que acabamos de crear. Finalmente, establecemos el formateador principal del eje y al objeto `Tick`.
