# Méthodes de chaîne de caractères

Les chaînes de caractères ont des méthodes qui effectuent diverses opérations sur les données de chaîne.

Exemple : enlever tout espace blanc en début / fin.

```python
s ='  Hello '
t = s.strip()     # 'Hello'
```

Exemple : conversion de cas.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Exemple : remplacement de texte.

```python
s = 'Hello world'
t = s.replace('Hello', 'Hallo')   # 'Hallo world'
```

**Plus de méthodes de chaîne de caractères** :

Les chaînes de caractères ont une grande variété d'autres méthodes pour tester et manipuler les données de texte. Voici un petit échantillon de méthodes :

```python
s.endswith(suffix)     # Vérifier si la chaîne se termine par suffix
s.find(t)              # Première occurrence de t dans s
s.index(t)             # Première occurrence de t dans s
s.isalpha()            # Vérifier si les caractères sont alphabétiques
s.isdigit()            # Vérifier si les caractères sont numériques
s.islower()            # Vérifier si les caractères sont en minuscules
s.isupper()            # Vérifier si les caractères sont en majuscules
s.join(slist)          # Joindre une liste de chaînes de caractères en utilisant s comme délimiteur
s.lower()              # Convertir en minuscules
s.replace(old,new)     # Remplacer du texte
s.rfind(t)             # Rechercher t à partir de la fin de la chaîne
s.rindex(t)            # Rechercher t à partir de la fin de la chaîne
s.split([delim])       # Diviser la chaîne en une liste de sous-chaînes
s.startswith(prefix)   # Vérifier si la chaîne commence par prefix
s.strip()              # Enlever les espaces blancs en début / fin
s.upper()              # Convertir en majuscules
```
