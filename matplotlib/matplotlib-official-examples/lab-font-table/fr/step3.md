# Afficher le tableau de caractères

Dans cette étape, nous allons utiliser `argparse` pour analyser le chemin vers le fichier de police à partir des arguments de ligne de commande. Ensuite, nous appellerons `print_glyphs` pour afficher tous les glyphes du fichier de police et `draw_font_table` pour dessiner le tableau de caractères des 255 premiers caractères de la police.

```python
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Afficher un tableau de caractères.")
    parser.add_argument("path", nargs="?", help="Chemin vers le fichier de police.")
    parser.add_argument("--print-all", action="store_true",
                        help="En outre, afficher tous les caractères sur la sortie standard.")
    args = parser.parse_args()

    if args.print_all:
        print_glyphs(args.path)
    draw_font_table(args.path)
```
