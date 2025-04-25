# フォントテーブルを表示する

このステップでは、`argparse`を使ってコマンドライン引数からフォントファイルへのパスを解析します。そして、フォントファイル内のすべてのグリフを表示するために`print_glyphs`を呼び出し、フォントの最初の 255 文字のフォントテーブルを描画するために`draw_font_table`を呼び出します。

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
