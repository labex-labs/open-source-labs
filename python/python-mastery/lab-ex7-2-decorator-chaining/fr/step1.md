# Copie des métadonnées

Lorsqu'une fonction est enveloppée par un décorateur, vous perdez souvent des informations sur le nom de la fonction, les chaînes de documentation et autres détails. Vérifiez cela :

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... regardez la sortie...
>>>
```

Corrigez la définition du décorateur `logged` de manière à ce qu'il copie correctement les métadonnées de la fonction. Pour ce faire, utilisez le décorateur `@wraps(func)` tel qu'indiqué dans les notes.

Une fois que vous avez terminé, assurez-vous que le décorateur conserve le nom de la fonction et la chaîne de documentation.

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

Corrigez le décorateur `@validated` que vous avez écrit précédemment de manière à ce qu'il conserve également les métadonnées en utilisant `@wraps(func)`.
