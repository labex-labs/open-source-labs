# Style du bas vers le haut

Les fonctions sont considérées comme des briques de construction. Les blocs les plus petits/les plus simples sont placés en premier.

```python
# myprogram.py
def foo(x):
  ...

def bar(x):
  ...
    foo(x)          # Défini ci-dessus
  ...

def spam(x):
  ...
    bar(x)          # Défini ci-dessus
  ...

spam(42)            # Le code qui utilise les fonctions apparaît à la fin
```

Les fonctions ultérieures s'appuient sur les fonctions antérieures. Encore une fois, il s'agit seulement d'un point de style. Le seul élément important dans le programme ci-dessus est que l'appel à `spam(42)` soit placé en dernier.
