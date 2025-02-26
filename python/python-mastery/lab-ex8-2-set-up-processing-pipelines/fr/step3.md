# Continuer

Oh, vous pouvez faire mieux que ça. Plongeons ceci dans votre code de génération de table. Modifiez le programme comme suit :

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

Cela devrait produire une sortie ressemblant à ceci :

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

Maintenant, C'EST FOU! Et assez génial.

**Discussion**

Certains enseignements à retenir : Vous pouvez créer diverses fonctions génératrices et les chaîner ensemble pour effectuer des traitements impliquant des pipelines de flux de données.

Un bon modèle mental pour les fonctions génératrices pourrait être des briques Lego. Vous pouvez créer une collection de petits modèles d'itérateurs et commencer à les empiler les uns sur les autres de diverses manières. C'est un moyen d'écrire des programmes extrêmement puissant.
