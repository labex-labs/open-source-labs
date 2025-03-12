# Utilisation du module inspect

En Python, la bibliothèque standard comprend un module `inspect` très utile. Ce module est comme un outil de détective qui nous aide à collecter des informations sur les objets en temps réel (live objects) en Python. Les objets en temps réel peuvent être des modules, des classes et des fonctions. Au lieu de fouiller manuellement dans les attributs d'un objet pour trouver des informations, le module `inspect` offre des méthodes plus organisées et de haut niveau pour comprendre les propriétés des fonctions.

Continuons d'utiliser le même shell interactif Python pour explorer le fonctionnement de ce module.

## Signatures de fonction

La fonction `inspect.signature()` est un outil pratique. Lorsque vous lui passez une fonction, elle retourne un objet `Signature`. Cet objet contient des détails importants sur les paramètres de la fonction.

Voici un exemple. Supposons que nous ayons une fonction nommée `add`. Nous pouvons utiliser la fonction `inspect.signature()` pour obtenir sa signature :

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

Lorsque vous exécutez ce code, le résultat sera :

```
(x, y)
```

Ce résultat nous montre la signature de la fonction, qui nous indique quels paramètres la fonction peut accepter.

## Examen des détails des paramètres

Nous pouvons aller plus loin et obtenir des informations plus approfondies sur chaque paramètre de la fonction.

```python
print(sig.parameters)
```

Le résultat de ce code sera :

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

Les paramètres de la fonction sont stockés dans un dictionnaire ordonné. Parfois, nous pouvons être seulement intéressés par les noms des paramètres. Nous pouvons convertir ce dictionnaire ordonné en un tuple pour extraire seulement les noms des paramètres.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

Le résultat sera :

```
('x', 'y')
```

## Examen des paramètres individuels

Nous pouvons également examiner de plus près chaque paramètre individuel. Le code suivant parcourt chaque paramètre de la fonction et affiche quelques détails importants à son sujet.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

Ce code nous montrera des détails sur chaque paramètre. Il nous indique le type de paramètre (s'il s'agit d'un paramètre positionnel, d'un paramètre mot - clé, etc.) et sa valeur par défaut s'il en a une.

Le module `inspect` a de nombreuses autres fonctions utiles pour l'introspection des fonctions. Voici quelques exemples :

- `inspect.getdoc(obj)` : Cette fonction récupère la chaîne de documentation pour un objet. Les chaînes de documentation sont comme des notes que les programmeurs écrivent pour expliquer ce que fait un objet.
- `inspect.getfile(obj)` : Elle nous aide à trouver le fichier où un objet est défini. Cela peut être très utile lorsque nous voulons localiser le code source d'un objet.
- `inspect.getsource(obj)` : Cette fonction récupère le code source d'un objet. Elle nous permet de voir exactement comment l'objet est implémenté.
