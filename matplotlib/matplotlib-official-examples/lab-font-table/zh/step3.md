# 显示字体表

在这一步中，我们将使用 `argparse` 从命令行参数中解析字体文件的路径。然后我们将调用 `print_glyphs` 来打印字体文件中的所有字形，并调用 `draw_font_table` 来绘制该字体的前 255 个字符的字体表。

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
