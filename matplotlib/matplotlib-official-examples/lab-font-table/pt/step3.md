# Exibir a tabela de fontes

Nesta etapa, usaremos `argparse` para analisar o caminho para o arquivo de fonte a partir dos argumentos da linha de comando. Em seguida, chamaremos `print_glyphs` para imprimir todos os glifos no arquivo de fonte e `draw_font_table` para desenhar a tabela de fontes dos primeiros 255 caracteres da fonte.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Exibir uma tabela de fontes.")
    parser.add_argument("path", nargs="?", help="Caminho para o arquivo de fonte.")
    parser.add_argument("--print-all", action="store_true",
                        help="Adicionalmente, imprimir todos os caracteres para stdout.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```
