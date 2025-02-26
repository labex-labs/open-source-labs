# Définir des fonctions

Il est une bonne idée de regrouper tout le code lié à une seule _tâche_ dans un seul endroit. Utilisez une fonction.

```python
def lire_prix(nom_fichier):
    prix = {}
    with open(nom_fichier) as f:
        f_csv = csv.reader(f)
        for ligne in f_csv:
            prix[ligne[0]] = float(ligne[1])
    return prix
```

Une fonction simplifie également les opérations répétées.

```python
anciens_prix = lire_prix('anciens_prix.csv')
nouveaux_prix = lire_prix('nouveaux_prix.csv')
```
