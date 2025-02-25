# Un programme d'exemple

Résolvons le problème suivant :

> Un matin, vous sortez et placez un billet de dollar sur le trottoir près de la Tour Sears à Chicago. Chaque jour après, vous sortez et doublez le nombre de billets. Combien de temps faut-il pour que la pile de billets dépasse la hauteur de la tour?

Voici une solution pour créer un fichier `sears.py` dans le répertoire `/home/labex/project` :

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Mètres (0,11 mm)
sears_height = 442 # Hauteur (mètres)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Nombre de jours', day)
print('Nombre de billets', num_bills)
print('Hauteur finale', num_bills * bill_thickness)
```

Lorsque vous l'exécutez, vous obtenez la sortie suivante :

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Nombre de jours 23
Nombre de billets 4194304
Hauteur finale 461.37344
```

En utilisant ce programme comme guide, vous pouvez apprendre un certain nombre de concepts clés importants sur Python.
