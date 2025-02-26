# Le débogueur Python

Vous pouvez lancer manuellement le débogueur à l'intérieur d'un programme.

```python
def some_function():
 ...
    breakpoint()      # Entrez dans le débogueur (Python 3.7+)
 ...
```

Cela lance le débogueur au niveau de l'appel `breakpoint()`.

Dans les versions antérieures de Python, vous faisiez ainsi. Vous verrez parfois cela mentionné dans d'autres guides de débogage.

```python
import pdb
...
pdb.set_trace()       # Au lieu de `breakpoint()`
...
```
