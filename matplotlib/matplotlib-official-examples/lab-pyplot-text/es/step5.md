# Agregar título, etiqueta del eje X y etiqueta del eje Y

Podemos agregar un título, una etiqueta del eje X y una etiqueta del eje Y al gráfico utilizando los métodos `title()`, `xlabel()` y `ylabel()` de la biblioteca `pyplot`. Agregaremos "Voltage vs Time" como título, "Time [s]" como etiqueta del eje X y "Voltage [mV]" como etiqueta del eje Y.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```
