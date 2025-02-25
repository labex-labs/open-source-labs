# Mostrar la tabla de fuentes

En este paso, usaremos `argparse` para analizar la ruta al archivo de fuente a partir de los argumentos de línea de comandos. Luego llamaremos a `print_glyphs` para imprimir todos los glifos del archivo de fuente y a `draw_font_table` para dibujar la tabla de fuentes de los primeros 255 caracteres de la fuente.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Mostrar una tabla de fuentes.")
    parser.add_argument("path", nargs="?", help="Ruta al archivo de fuente.")
    parser.add_argument("--print-all", action="store_true",
                        help="Además, imprima todos los caracteres a la salida estándar.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```
