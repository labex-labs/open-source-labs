# Zeige die Schrifttabelle an

In diesem Schritt werden wir `argparse` verwenden, um den Pfad zur Schriftdatei aus den Befehlszeilenargumenten zu analysieren. Anschließend werden wir `print_glyphs` aufrufen, um alle Glyphen in der Schriftdatei auszugeben, und `draw_font_table`, um die Schrifttabelle der ersten 255 Zeichen der Schrift zu zeichnen.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Zeige eine Schrifttabelle an.")
    parser.add_argument("path", nargs="?", help="Pfad zur Schriftdatei.")
    parser.add_argument("--print-all", action="store_true",
                        help="Optional: Drucke alle Zeichen auf die Standardeingabe aus.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```
