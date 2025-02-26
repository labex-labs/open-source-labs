# Valeurs d'exception

Les exceptions ont une valeur associée. Elle contient des informations plus spécifiques sur ce qui ne va pas.

```python
raise RuntimeError('Invalid user name')
```

Cette valeur est partie de l'instance d'exception qui est placée dans la variable fournie à `except`.

```python
try:
 ...
except RuntimeError as e:   # `e` contient l'exception levée
 ...
```

`e` est une instance du type d'exception. Cependant, elle semble souvent une chaîne de caractères lorsqu'elle est affichée.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
