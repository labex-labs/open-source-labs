# Travailler avec les chaînes de caractères (strings) en Python

Les chaînes de caractères sont l'un des types de données les plus couramment utilisés en Python. Elles servent à représenter du texte et peuvent contenir des lettres, des nombres et des symboles. Dans cette étape, nous allons explorer diverses opérations sur les chaînes de caractères, qui sont des compétences essentielles pour travailler avec des données textuelles en Python.

## Création et définition de chaînes de caractères

Pour commencer à travailler avec les chaînes de caractères en Python, nous devons d'abord ouvrir un shell interactif Python. Ce shell nous permet d'écrire et d'exécuter du code Python ligne par ligne, ce qui est idéal pour apprendre et tester. Ouvrez un shell interactif Python à nouveau en utilisant la commande suivante :

```bash
python3
```

Une fois le shell ouvert, nous pouvons définir une chaîne de caractères. Dans cet exemple, nous allons créer une chaîne de caractères qui contient des symboles de titres boursiers. Une chaîne de caractères en Python peut être définie en entourant le texte de guillemets simples (`'`) ou de guillemets doubles (`"`). Voici comment nous définissons notre chaîne de caractères :

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

Nous avons maintenant créé une variable de type chaîne de caractères nommée `symbols` et lui avons assigné une valeur. Lorsque nous tapons le nom de la variable et appuyons sur Entrée, Python affiche la valeur de la chaîne de caractères.

## Accès aux caractères et aux sous-chaînes

En Python, les chaînes de caractères peuvent être indexées pour accéder à des caractères individuels. L'indexation commence à 0, ce qui signifie que le premier caractère d'une chaîne de caractères a un index de 0, le deuxième a un index de 1, et ainsi de suite. L'indexation négative est également prise en charge, où -1 fait référence au dernier caractère, -2 au avant-dernier caractère, et ainsi de suite.

Voyons comment nous pouvons accéder à des caractères individuels dans notre chaîne de caractères `symbols` :

```python
>>> symbols[0]    # Premier caractère
'A'
>>> symbols[1]    # Deuxième caractère
'A'
>>> symbols[2]    # Troisième caractère
'P'
>>> symbols[-1]   # Dernier caractère
'O'
>>> symbols[-2]   # Avant-dernier caractère
'C'
```

Nous pouvons également extraire des sous-chaînes en utilisant le découpage (slicing). Le découpage nous permet d'obtenir une partie de la chaîne de caractères en spécifiant un index de départ et un index de fin. La syntaxe pour le découpage est `string[start:end]`, où la sous-chaîne inclut les caractères de l'index de départ jusqu'à (mais sans inclure) l'index de fin.

```python
>>> symbols[:4]    # Les 4 premiers caractères
'AAPL'
>>> symbols[-3:]   # Les 3 derniers caractères
'SCO'
>>> symbols[5:8]   # Les caractères de l'index 5 à 7
'IBM'
```

## Immutabilité des chaînes de caractères

Les chaînes de caractères en Python sont immuables, ce qui signifie qu'une fois qu'une chaîne de caractères est créée, vous ne pouvez pas modifier ses caractères individuels. Si vous essayez de modifier un caractère dans une chaîne de caractères, Python lèvera une erreur.

Essayons de changer le premier caractère de notre chaîne de caractères `symbols` :

```python
>>> symbols[0] = 'a'    # Cela causera une erreur
```

Vous devriez voir une erreur comme celle-ci :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Cette erreur indique que nous ne pouvons pas assigner une nouvelle valeur à un caractère individuel dans une chaîne de caractères car les chaînes de caractères sont immuables.

## Concaténation de chaînes de caractères

Bien que nous ne puissions pas modifier directement les chaînes de caractères, nous pouvons créer de nouvelles chaînes de caractères par concaténation. La concaténation consiste à joindre deux ou plusieurs chaînes de caractères ensemble. En Python, nous pouvons utiliser l'opérateur `+` pour concaténer des chaînes de caractères.

```python
>>> symbols += ' GOOG'    # Ajouter un nouveau symbole
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Ajouter un nouveau symbole au début
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Il est important de se rappeler que ces opérations créent de nouvelles chaînes de caractères plutôt que de modifier la chaîne de caractères originale. La chaîne de caractères originale reste inchangée, et une nouvelle chaîne de caractères est créée avec la valeur combinée.

## Vérification de l'existence de sous-chaînes

Pour vérifier si une sous-chaîne existe dans une chaîne de caractères, nous pouvons utiliser l'opérateur `in`. L'opérateur `in` retourne `True` si la sous-chaîne est trouvée dans la chaîne de caractères et `False` sinon.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Notez que 'AA' retourne `True` car il est trouvé dans "AAPL". C'est un moyen utile de rechercher un texte spécifique dans une chaîne de caractères plus longue.

## Méthodes des chaînes de caractères

Les chaînes de caractères en Python sont dotées de nombreuses méthodes intégrées qui nous permettent d'effectuer diverses opérations sur les chaînes de caractères. Ces méthodes sont des fonctions associées à l'objet chaîne de caractères et peuvent être appelées en utilisant la notation pointée (`string.method()`).

```python
>>> symbols.lower()    # Convertir en minuscules
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # La chaîne de caractères originale reste inchangée
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # Sauvegarder le résultat dans une nouvelle variable
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # Trouver l'index de départ d'une sous-chaîne
13
>>> symbols[13:17]    # Vérifier la sous-chaîne à cette position
'MSFT'

>>> symbols = symbols.replace('SCO','')    # Remplacer une sous-chaîne
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

Lorsque vous avez terminé vos expériences, vous pouvez quitter le shell Python en utilisant la commande suivante :

```python
>>> exit()
```
