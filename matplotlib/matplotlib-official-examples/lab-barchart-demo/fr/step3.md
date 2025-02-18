# Définition des fonctions auxiliaires

Nous définissons deux fonctions auxiliaires. La première fonction, `to_ordinal`, convertit un entier en une chaîne de caractères ordinale (par exemple, 2 -> '2ème'). La deuxième fonction, `format_score`, crée des étiquettes de score pour l'axe des ordonnées droit sous la forme du nom du test suivi de l'unité de mesure (le cas échéant), réparties sur deux lignes.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
