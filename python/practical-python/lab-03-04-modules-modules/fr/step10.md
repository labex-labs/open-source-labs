# Recherche des modules

Python consulte une liste de chemins (`sys.path`) lorsqu'il recherche des modules.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

Le répertoire de travail actuel est généralement le premier.
