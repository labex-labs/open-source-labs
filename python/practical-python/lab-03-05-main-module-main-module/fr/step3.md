# Vérification de `__main__`

Il est une pratique standard pour les modules exécutés en tant que script principal d'utiliser cette convention :

```python
# prog.py
...
if __name__ == '__main__':
    # Exécuté en tant que programme principal...
    instructions
  ...
```

Les instructions incluses à l'intérieur de l'instruction `if` deviennent le _programme principal_.
