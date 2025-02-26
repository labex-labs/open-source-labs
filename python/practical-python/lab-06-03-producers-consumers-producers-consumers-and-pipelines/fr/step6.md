# Exercice 6.11 : Filtrer des données

Écrivez une fonction qui filtre des données. Par exemple :

```python
# ticker.py
...

def filtrer_symboles(lignes, noms):
    for ligne in lignes:
        if ligne['GOOG'] in noms:
            yield ligne
```

Utilisez cela pour filtrer les actions uniquement celles de votre portefeuille :

```python
import rapport
import cotation
import suivre
portefeuille = rapport.lire_portefeuille('portefeuille.csv')
lignes = cotation.parser_données_boursières(suivre.suivre('stocklog.csv'))
lignes = cotation.filtrer_symboles(lignes, portefeuille)
for ligne in lignes:
    print(ligne)
```
