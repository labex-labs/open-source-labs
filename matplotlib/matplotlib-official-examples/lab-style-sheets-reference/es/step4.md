# Trazar la figura de demostración para cada hoja de estilo

Finalmente, debes trazar la figura de demostración para cada hoja de estilo disponible. Puedes hacer esto recorriendo la `style_list` y llamando a la función `plot_figure()` para cada hoja de estilo.

```python
if __name__ == "__main__":

    # Configura una lista de todos los estilos disponibles, en orden alfabético pero
    # los estilos `default` y `classic`, que se colocarán respectivamente en
    # la primera y segunda posición.
    # Los estilos con guiones bajos al principio son para uso interno, como pruebas
    # y galerías de tipos de trazado. Estos se excluyen aquí.
    style_list = ['default', 'classic'] + sorted(
        style for style in plt.style.available
        if style!= 'classic' and not style.startswith('_'))

    # Traza una figura de demostración para cada hoja de estilo disponible.
    for style_label in style_list:
        with plt.rc_context({"figure.max_open_warning": len(style_list)}):
            with plt.style.context(style_label):
                plot_figure(style_label=style_label)

    plt.show()
```
