# Les modules comme environnements

Les modules forment un environnement entourant tout le code défini à l'intérieur.

```python
# foo.py
x = 42

def grok(a):
    print(x)
```

Les variables _globales_ sont toujours liées au module entourant (même fichier). Chaque fichier source est son propre petit univers.
