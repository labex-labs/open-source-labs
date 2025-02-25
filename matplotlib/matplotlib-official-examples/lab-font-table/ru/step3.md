# Отобразить таблицу шрифта

В этом шаге мы будем использовать `argparse` для разбора пути к файлу шрифта из аргументов командной строки. Затем мы вызовем `print_glyphs`, чтобы распечатать все глифы в файле шрифта, и `draw_font_table`, чтобы нарисовать таблицу шрифта первых 255 символов шрифта.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Display a font table.")
    parser.add_argument("path", nargs="?", help="Path to the font file.")
    parser.add_argument("--print-all", action="store_true",
                        help="Additionally, print all chars to stdout.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```
