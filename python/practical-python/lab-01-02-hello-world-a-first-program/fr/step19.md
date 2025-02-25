# Exercice 1.6 : Débogage

Le fragment de code suivant contient du code du problème de la tour Sears. Il y a également un bogue dedans.

```python
# sears.py

bill_thickness = 0.11 * 0.001    # Mètres (0.11 mm)
sears_height   = 442             # Hauteur (mètres)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = days + 1
    num_bills = num_bills * 2

print('Nombre de jours', day)
print('Nombre de billets', num_bills)
print('Hauteur finale', num_bills * bill_thickness)
```

Copiez et collez le code ci-dessus dans un nouveau programme appelé `sears.py`. Lorsque vous exécutez le code, vous obtiendrez un message d'erreur qui fera planter le programme comme ceci :

```code
Traceback (most recent call last):
  File "sears.py", line 10, in <module>
    day = days + 1
NameError: name 'days' is not defined
```

La lecture des messages d'erreur est une partie importante du code Python. Si votre programme plante, la dernière ligne du message de traceback est la véritable raison pour laquelle le programme est tombé en panne. Au-dessus de cela, vous devriez voir un fragment de code source puis un nom de fichier et un numéro de ligne identifiants.

- Quelle est la ligne avec l'erreur?
- Quel est l'erreur?
- Corrigez l'erreur
- Exécutez le programme avec succès
