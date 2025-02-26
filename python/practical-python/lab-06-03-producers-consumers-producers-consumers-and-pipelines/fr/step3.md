# Exercice 6.8 : Configuration d'un pipeline simple

Voyons cette idée de pipeline en action. Écrivez la fonction suivante :

```python
>>> def filematch(lignes, sous_chaîne):
        for ligne in lignes:
            if sous_chaîne in ligne:
                yield ligne

>>>
```

Cette fonction est presque exactement la même que le premier exemple de générateur de l'exercice précédent, sauf qu'elle n'ouvre plus un fichier - elle opère simplement sur une séquence de lignes passée en argument. Maintenant, essayez ceci :

```python
>>> from suivre import suivre
>>> lignes = suivre('stocklog.csv')
>>> goog = filematch(lignes, 'GOOG')
>>> for ligne in goog:
        print(ligne)

... attendez la sortie...
```

Il peut prendre un certain temps pour que la sortie apparaisse, mais finalement vous devriez voir quelques lignes contenant des données pour GOOG.

Note : Ces exercices doivent être exécutés simultanément sur deux terminaux distincts.
