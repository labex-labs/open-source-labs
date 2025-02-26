# Classe de base `object`

Si une classe n'a pas de parent, vous voyez parfois `object` utilisé comme base.

```python
class Shape(object):
...
```

`object` est le parent de tous les objets en Python.

\*Note : techniquement, ce n'est pas obligatoire, mais vous le voyez souvent spécifié comme héritage de son utilisation obligatoire en Python 2. Si omis, la classe hérite implicitement de `object`.
