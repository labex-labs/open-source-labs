# La ligne `#!`

Sur Unix, la ligne `#!` peut lancer un script en tant que Python. Ajoutez ce qui suit à la première ligne de votre fichier de script.

```python
#!/usr/bin/env python3
#./prog.py
...
```

Elle nécessite les permissions d'exécution.

```bash
$ chmod +x prog.py
# Ensuite, vous pouvez exécuter
$./prog.py
... sortie...
```

_Nota : Le lanceur Python sous Windows recherche également la ligne `#!` pour indiquer la version de langage._
