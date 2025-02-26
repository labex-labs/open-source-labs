# Instruction `with`

Dans le code moderne, `try-finally` est souvent remplacé par l'instruction `with`.

```python
lock = Lock()
with lock:
    # verrou acquis
  ...
# verrou libéré
```

Un exemple plus familier :

```python
with open(filename) as f:
    # Utiliser le fichier
  ...
# Fichier fermé
```

`with` définit un _contexte_ d'utilisation pour une ressource. Lorsque l'exécution quitte ce contexte, les ressources sont libérées. `with` ne fonctionne qu'avec certains objets qui ont été spécifiquement programmés pour le supporter.
