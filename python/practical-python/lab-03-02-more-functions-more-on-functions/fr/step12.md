# Reaffectation vs Modification

Assurez-vous de comprendre la subtile différence entre modifier une valeur et réaffecter un nom de variable.

```python
def foo(items):
    items.append(42)    # Modifie l'objet d'entrée

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# CONTRARES
def bar(items):
    items = [4,5,6]    # Change la variable locale `items` pour qu'elle pointe vers un autre objet

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

_Rappel : L'affectation de variable n'écrase jamais la mémoire. Le nom est simplement lié à une nouvelle valeur._

Cet ensemble d'exercices vous demande de mettre en œuvre ce qui est peut-être la partie la plus puissante et la plus difficile du cours. Il y a beaucoup d'étapes et de nombreux concepts des exercices précédents sont combinés tous à la fois. La solution finale n'est que d'environ 25 lignes de code, mais prenez votre temps et assurez-vous de comprendre chaque partie.

Une partie centrale de votre programme `report.py` porte sur la lecture de fichiers CSV. Par exemple, la fonction `read_portfolio()` lit un fichier contenant des lignes de données de portefeuille et la fonction `read_prices()` lit un fichier contenant des lignes de données de prix. Dans les deux fonctions, il y a beaucoup de parties "fastidieuses" de bas niveau et des fonctionnalités similaires. Par exemple, elles ouvrent toutes deux un fichier et l'enveloppent avec le module `csv` et elles convertissent tous deux divers champs en nouveaux types.

Si vous deviez faire beaucoup d'analyse de fichiers dans la réalité, vous voudriez probablement nettoyer certaines de ces parties et la rendre plus générique. C'est notre objectif.

Commencez cet exercice en ouvrant le fichier appelé `fileparse.py`. C'est là que nous allons travailler.
