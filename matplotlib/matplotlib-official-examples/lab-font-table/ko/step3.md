# 폰트 테이블 표시

이 단계에서는 `argparse`를 사용하여 명령줄 인자에서 폰트 파일의 경로를 파싱합니다. 그런 다음 `print_glyphs`를 호출하여 폰트 파일의 모든 글리프를 출력하고, `draw_font_table`을 호출하여 폰트의 처음 255 개 문자에 대한 폰트 테이블을 그립니다.

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
