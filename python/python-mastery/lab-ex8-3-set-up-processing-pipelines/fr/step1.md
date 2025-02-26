# Un exemple de coroutine

Commencer avec les coroutines peut être un peu difficile. Voici un programme d'exemple qui effectue la même tâche que l'exercice 8.2, mais avec des coroutines. Prenez ce programme et copiez-le dans un fichier appelé `cofollow.py`.

```python
# cofollow.py
import os
import time

# Source de données
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# Décorateur pour les fonctions de coroutine
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Coroutine d'échantillonnage
@consumer
def printer():
    while True:
        item = yield     # Recevoir un élément envoyé à moi
        print(item)

# Utilisation exemple
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

Exécutez ce programme et assurez-vous qu'il produit une sortie. Assurez-vous de comprendre comment les différents morceaux sont accrochés ensemble.
