# Variables d'environnement

Les variables d'environnement sont définies dans le shell.

```bash
$ export NAME dave
$ export RSH ssh
$ python3 prog.py
```

`os.environ` est un dictionnaire qui contient ces valeurs.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Les modifications sont réflétées dans tous les sous-processus lancés ultérieurement par le programme.
