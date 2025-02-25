# Exercice 1.30 : Convertir un script en fonction

Prenez le code que vous avez écrit pour le programme `pcost.py` dans l'exercice 1.27 et convertissez-le en une fonction `portfolio_cost(filename)`. Cette fonction prend un nom de fichier en entrée, lit les données du portefeuille dans ce fichier et renvoie le coût total du portefeuille sous forme d'un nombre à virgule flottante.

Pour utiliser votre fonction, modifiez votre programme de sorte qu'il ressemble à ceci :

```python
# pcost.py
def portfolio_cost(filename):
    """
    Calcule le coût total (nombre d'actions * prix) d'un fichier de portefeuille
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Entrez un nom de fichier :")

cost = portfolio_cost(filename)
print("Coût total :", cost)
```

Lorsque vous exécutez votre programme, vous devriez voir la même sortie que précédemment. Après avoir exécuté votre programme, vous pouvez également appeler votre fonction de manière interactive en tapant ceci :

```bash
$ python3 -i pcost.py
```

Cela vous permettra d'appeler votre fonction à partir du mode interactif.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Être capable d'expérimenter avec votre code de manière interactive est utile pour le test et le débogage.
