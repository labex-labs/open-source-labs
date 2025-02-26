# Exercice 6.6 : Utilisation d'un générateur pour produire des données

Si vous examinez le code de l'Exercice 6.5, la première partie du code produit des lignes de données tandis que les instructions à la fin de la boucle `while` consomment les données. Une caractéristique majeure des fonctions génératrices est que vous pouvez déplacer tout le code de production de données dans une fonction réutilisable.

Modifiez le code de l'Exercice 6.5 de sorte que la lecture du fichier soit effectuée par une fonction génératrice `follow(filename)`. Assurez-vous que le code suivant fonctionne :

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Devrait voir des lignes de sortie produites ici...
```

Modifiez le code de la cotation boursière de sorte qu'il ressemble à ceci :

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
