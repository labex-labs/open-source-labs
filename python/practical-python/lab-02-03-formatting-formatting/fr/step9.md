# Exercice 2.11 : Ajout de quelques en-têtes

Supposons qu'on ait un tuple de noms d'en-tête comme ceci :

```python
entetes = ('Nom', 'Actions', 'Prix', 'Changement')
```

Ajoutez du code à votre programme qui prend le tuple d'en-têtes ci-dessus et crée une chaîne de caractères où chaque nom d'en-tête est aligné à droite dans un champ de 10 caractères de large et chaque champ est séparé par un espace unique.

```python
'      Nom     Actions      Prix      Changement'
```

Écrivez du code qui prend les en-têtes et crée la chaîne de caractères séparatrice entre les en-têtes et les données qui suivent. Cette chaîne de caractères est juste une série de caractères "-" sous chaque nom de champ. Par exemple :

```python
'---------- ---------- ---------- -----------'
```

Quand vous avez fini, votre programme devrait produire le tableau montré au début de cet exercice.

          Nom     Actions      Prix     Changement
    ---------- ---------- ---------- ----------
            AA        100       9,22     -22,98
           IBM         50     106,28      15,18
           CAT        150      35,46     -47,98
          MSFT        200      20,89     -30,34
            GE         95      13,48     -26,89
          MSFT         50      20,89     -44,21
           IBM        100     106,28      35,84
