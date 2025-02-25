# Instruction `break`

Vous pouvez utiliser l'instruction `break` pour sortir d'une boucle prématurément.

```python
for name in namelist:
    if name == 'Jake':
        break
  ...
  ...
statements
```

Lorsque l'instruction `break` est exécutée, elle sort de la boucle et passe aux `statements` suivants. L'instruction `break` ne s'applique qu'à la boucle la plus interne. Si cette boucle se trouve à l'intérieur d'une autre boucle, elle n'arrêtera pas la boucle externe.
