# Display the font table

In this step, we will use `argparse` to parse the path to the font file from the command-line arguments. Then we will call `print_glyphs` to print all the glyphs in the font file, and `draw_font_table` to draw the font table of the first 255 characters of the font.

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
