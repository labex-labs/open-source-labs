# Un peu d'art génératif

Créez le programme suivant et mettez-le dans un fichier appelé `art.py` :

```python
# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
```

Assurez-vous que vous pouvez exécuter ce programme à partir de la ligne de commande ou d'un terminal.

```bash
python3 art.py 10 20
```

Si vous exécutez la commande ci-dessus, vous obtiendrez un message d'erreur et de traceback. Corrigez le problème et exécutez le programme à nouveau. Vous devriez obtenir une sortie comme celle-ci :

```bash
python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|
```

## Note importante

Il est absolument essentiel que vous soyez capable d'éditer, d'exécuter et de déboguer des programmes Python ordinaires pour le reste de ce cours. Le choix d'un éditeur, d'un IDE ou d'un système d'exploitation n'a pas d'importance, pourvu que vous soyez capable d'expérimenter de manière interactive et de créer des fichiers sources Python normaux qui peuvent être exécutés à partir de la ligne de commande.
