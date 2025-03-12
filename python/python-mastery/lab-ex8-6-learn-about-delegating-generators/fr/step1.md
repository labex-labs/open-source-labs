# Comprendre l'instruction `yield from`

Dans cette étape, nous allons explorer l'instruction `yield from` en Python. Cette instruction est un outil puissant lorsqu'on travaille avec des générateurs, et elle simplifie le processus de délégation d'opérations à d'autres générateurs. À la fin de cette étape, vous comprendrez ce que `yield from` est, comment il fonctionne et comment il peut gérer le passage de valeurs entre différents générateurs.

## Qu'est-ce que `yield from` ?

L'instruction `yield from` a été introduite en Python 3.3. Son principal but est de simplifier la délégation d'opérations aux sous-générateurs. Un sous-générateur est simplement un autre générateur auquel un générateur principal peut déléguer du travail.

Normalement, lorsque vous voulez qu'un générateur produise des valeurs issues d'un autre générateur, vous devez utiliser une boucle. Par exemple, sans `yield from`, vous écrirez du code comme ceci :

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

Dans ce code, le `delegating_generator` utilise une boucle `for` pour itérer sur les valeurs produites par `subgenerator` puis produit chaque valeur une par une.

Cependant, avec l'instruction `yield from`, le code devient beaucoup plus simple :

```python
def delegating_generator():
    yield from subgenerator()
```

Cette seule ligne de code atteint le même résultat que la boucle de l'exemple précédent. Mais `yield from` n'est pas seulement un raccourci. Il gère également la communication bidirectionnelle entre l'appelant et le sous-générateur. Cela signifie que toutes les valeurs envoyées au générateur déléguant sont passées directement au sous-générateur.

## Exemple de base

Créons un exemple simple pour voir comment `yield from` fonctionne en pratique.

1. Tout d'abord, nous devons ouvrir le fichier `cofollow.py` dans l'éditeur. Pour ce faire, nous allons utiliser la commande `cd` pour naviguer jusqu'au bon répertoire. Exécutez la commande suivante dans le terminal :

```bash
cd /home/labex/project
```

2. Ensuite, nous allons ajouter deux fonctions au fichier `cofollow.py`. La fonction `subgen` est un simple générateur qui produit les nombres de 0 à 4. La fonction `main_gen` utilise `yield from` pour déléguer la génération de ces nombres à `subgen` puis produit la chaîne de caractères `'Done'`. Ajoutez le code suivant à la fin du fichier `cofollow.py` :

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. Maintenant, testons ces fonctions. Ouvrez un interpréteur Python et exécutez le code suivant :

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

Lorsque vous exécutez ce code, vous devriez voir la sortie suivante :

```
0
1
2
3
4

0
1
2
3
4
Done
```

Cette sortie montre que `yield from` permet à `main_gen` de passer toutes les valeurs générées par `subgen` directement à l'appelant.

## Passage de valeurs avec `yield from`

L'une des fonctionnalités les plus puissantes de `yield from` est sa capacité à gérer le passage de valeurs dans les deux sens. Créons un exemple plus complexe pour démontrer cela.

1. Ajoutez les fonctions suivantes au fichier `cofollow.py` :

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

La fonction `accumulator` est une coroutine qui suit un total courant. Elle produit le total actuel puis attend de recevoir une nouvelle valeur. Si elle reçoit `None`, elle arrête la boucle. La fonction `caller` crée une instance de `accumulator` et utilise `yield from` pour déléguer toutes les opérations d'envoi et de réception à elle.

2. Testez ces fonctions dans un interpréteur Python :

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

Lorsque vous exécutez ce code, vous devriez voir la sortie suivante :

```
0
1
3
6
'Total accumulated'
```

Cette sortie montre que `yield from` délègue entièrement toutes les opérations d'envoi et de réception au sous-générateur jusqu'à ce qu'il soit épuisé.

Maintenant que vous comprenez les bases de `yield from`, nous passerons à des applications plus pratiques dans l'étape suivante.
