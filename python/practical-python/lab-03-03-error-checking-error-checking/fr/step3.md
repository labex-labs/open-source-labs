# Gestion d'exceptions

Les exceptions se propagent jusqu'au premier `except` correspondant.

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # Exception levée ici

def spam():
    grok()                        # Appel qui entraînera une exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception capturée ici
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # L'exception n'arrive PAS ici
      ...

foo()
```

Pour gérer l'exception, placez des instructions dans le bloc `except`. Vous pouvez ajouter n'importe quelles instructions pour gérer l'erreur.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception capturée ici
        instructions            # Utilisez ces instructions
        instructions
      ...

bar()
```

Après la gestion, l'exécution reprend avec la première instruction après le `try-except`.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception capturée ici
        instructions
        instructions
      ...
    instructions                  # Reprend l'exécution ici
    instructions                  # Et continue ici
  ...

bar()
```
