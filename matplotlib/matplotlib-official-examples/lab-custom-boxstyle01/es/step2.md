# Implementar un estilo de caja personalizado como una clase

Los estilos de caja personalizados también se pueden implementar como clases que implementen `__call__`. Las clases luego se pueden registrar en el diccionario `BoxStyle._style_list`, lo que permite especificar el estilo de caja como una cadena, `bbox=dict(boxstyle="nombre_registrado,param=valor,...",...)`.

```python
class MyStyle:
    """Una caja simple."""

    def __init__(self, pad=0.3):
        """
        Los argumentos deben ser números de punto flotante y tener valores predeterminados.

        Parámetros
        ----------
        pad : float
            Cantidad de relleno
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        Dada la ubicación y el tamaño de la caja, devuelve la ruta de la caja
        alrededor de ella.

        La rotación se maneja automáticamente.

        Parámetros
        ----------
        x0, y0, width, height : float
            Ubicación y tamaño de la caja.
        mutation_size : float
            Escala de referencia para la mutación, generalmente el tamaño de fuente del texto.
        """
        # padding
        pad = mutation_size * self.pad
        # width and height with padding added
        width = width + 2.*pad
        height = height + 2.*pad
        # boundary of the padded box
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # return the new path
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # Registra el estilo personalizado.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # Elimina el registro.

plt.show()
```
