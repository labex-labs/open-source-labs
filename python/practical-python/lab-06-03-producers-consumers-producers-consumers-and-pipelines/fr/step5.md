# Exercice 6.10 : Création de plus de composants de pipeline

Étendons l'idée globale en un pipeline plus important. Dans un fichier séparé `ticker.py`, commençons par créer une fonction qui lit un fichier CSV comme vous l'avez fait ci-dessus :

```python
# ticker.py

from suivre import suivre
import csv

def parser_données_boursières(lignes):
    lignes_csv = csv.reader(lignes)
    return lignes_csv

if __name__ == '__main__':
    lignes = suivre('stocklog.csv')
    lignes_csv = parser_données_boursières(lignes)
    for ligne_csv in lignes_csv:
        print(ligne_csv)
```

Écrivez une nouvelle fonction qui sélectionne des colonnes spécifiques :

    # ticker.py

...
def sélectionner_colonnes(lignes_csv, indices):
for ligne_csv in lignes_csv:
yield [ligne_csv[index] for index in indices]
...
def parser_données_boursières(lignes):
lignes_csv = csv.reader(lignes)
lignes_csv = sélectionner_colonnes(lignes_csv, [0, 1, 4])
return lignes_csv

Exécutez votre programme à nouveau. Vous devriez voir une sortie réduite comme ceci :

    ['GOOG', '1503.06', '2.81']
    ['AAPL', '253.31', '2.81']
    ['GOOG', '1503.07', '2.82']
    ['AAPL', '253.32', '2.82']
    ['GOOG', '1503.08', '2.83']

...

Écrivez des fonctions génératrices qui convertissent les types de données et construisent des dictionnaires. Par exemple :

```python
# ticker.py
...

def convertir_types(lignes_csv, types):
    for ligne_csv in lignes_csv:
        yield [func(val) for func, val in zip(types, ligne_csv)]

def créer_dictionnaires(lignes_csv, en-têtes):
    for ligne_csv in lignes_csv:
        yield dict(zip(en-têtes, ligne_csv))
...
def parser_données_boursières(lignes):
    lignes_csv = csv.reader(lignes)
    lignes_csv = sélectionner_colonnes(lignes_csv, [0, 1, 4])
    lignes_csv = convertir_types(lignes_csv, [str, float, float])
    lignes_csv = créer_dictionnaires(lignes_csv, ['nom', 'prix', 'variation'])
    return lignes_csv
...
```

Exécutez votre programme à nouveau. Vous devriez maintenant avoir un flux de dictionnaires comme ceci :

    {'nom': 'GOOG', 'prix': 1503.4, 'variation': 3.15}
    {'nom': 'AAPL', 'prix': 253.65, 'variation': 3.15}
    {'nom': 'GOOG', 'prix': 1503.41, 'variation': 3.16}
    {'nom': 'AAPL', 'prix': 253.66, 'variation': 3.16}
    {'nom': 'GOOG', 'prix': 1503.42, 'variation': 3.17}
    {'nom': 'AAPL', 'prix': 253.67, 'variation': 3.17}

...
