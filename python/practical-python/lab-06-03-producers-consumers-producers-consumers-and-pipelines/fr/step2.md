# Pipelines de générateurs

Vous pouvez utiliser cet aspect des générateurs pour créer des pipelines de traitement (comme les tubes Unix).

_producteur_ → _traitement_ → _traitement_ → _consommateur_

Les pipelines de traitement ont un producteur de données initial, un certain nombre d'étapes de traitement intermédiaires et un consommateur final.

**producteur** → _traitement_ → _traitement_ → _consommateur_

```python
def producteur():
 ...
    yield élément
 ...
```

Le producteur est généralement un générateur. Bien qu'il puisse également être une liste ou une autre séquence. `yield` alimente les données dans le pipeline.

_producteur_ → _traitement_ → _traitement_ → **consommateur**

```python
def consommateur(s):
    for élément in s:
     ...
```

Le consommateur est une boucle `for`. Il reçoit les éléments et fait quelque chose avec eux.

_producteur_ → **traitement** → **traitement** → _consommateur_

```python
def traitement(s):
    for élément in s:
     ...
        yield nouvelélément
     ...
```

Les étapes de traitement intermédiaires consomment et produisent simultanément des éléments. Elles peuvent modifier le flux de données. Elles peuvent également filtrer (en éliminant des éléments).

_producteur_ → _traitement_ → _traitement_ → _consommateur_

```python
def producteur():
 ...
    yield élément          # produit l'élément reçu par le `traitement`
 ...

def traitement(s):
    for élément in s:      # Vient du `producteur`
     ...
        yield nouvelélément   # produit un nouvel élément
     ...

def consommateur(s):
    for élément in s:      # Vient du `traitement`
     ...
```

Code pour configurer le pipeline

```python
a = producteur()
b = traitement(a)
c = consommateur(b)
```

Vous remarquerez que les données circulent progressivement à travers les différentes fonctions.

Pour cet exercice, le programme `stocksim.py` devrait toujours être exécuté en arrière-plan. Vous allez utiliser la fonction `suivre()` que vous avez écrite dans l'exercice précédent.
