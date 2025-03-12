# Mesure de l'utilisation mémoire avec différentes méthodes de stockage

Dans cette étape, nous allons examiner comment différentes manières de stocker des données peuvent avoir un impact sur l'utilisation mémoire. L'utilisation mémoire est un aspect important de la programmation, en particulier lorsqu'il s'agit de traiter de grands ensembles de données. Pour mesurer la mémoire utilisée par notre code Python, nous allons utiliser le module `tracemalloc` de Python. Ce module est très utile car il nous permet de suivre les allocations mémoire effectuées par Python. En l'utilisant, nous pouvons voir combien de mémoire nos méthodes de stockage de données consomment.

## Méthode 1 : Stockage du fichier entier sous forme d'une seule chaîne de caractères

Commençons par créer un nouveau fichier Python. Accédez au répertoire `/home/labex/project` et créez un fichier nommé `memory_test1.py`. Vous pouvez utiliser un éditeur de texte pour ouvrir ce fichier. Une fois le fichier ouvert, ajoutez le code suivant. Ce code lira le contenu entier d'un fichier sous forme d'une seule chaîne de caractères et mesurera l'utilisation mémoire.

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # Start tracking memory
    tracemalloc.start()

    # Read the entire file as a single string
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

Après avoir ajouté le code, enregistrez le fichier. Maintenant, pour exécuter ce script, ouvrez votre terminal et exécutez la commande suivante :

```bash
python3 /home/labex/project/memory_test1.py
```

Lorsque vous exécutez le script, vous devriez voir une sortie similaire à ceci :

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

Les nombres exacts peuvent différer sur votre système, mais généralement, vous remarquerez que l'utilisation mémoire actuelle est d'environ 12 Mo et l'utilisation mémoire maximale d'environ 24 Mo.

## Méthode 2 : Stockage sous forme de liste de chaînes de caractères

Ensuite, nous allons tester une autre manière de stocker les données. Créez un nouveau fichier nommé `memory_test2.py` dans le même répertoire `/home/labex/project`. Ouvrez ce fichier dans l'éditeur et ajoutez le code suivant. Ce code lit le fichier et stocke chaque ligne sous forme de chaîne de caractères distincte dans une liste, puis mesure l'utilisation mémoire.

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # Start tracking memory
    tracemalloc.start()

    # Read the file as a list of strings (one string per line)
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # Get memory usage statistics
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # Stop tracking memory
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

Enregistrez le fichier, puis exécutez le script en utilisant la commande suivante dans le terminal :

```bash
python3 /home/labex/project/memory_test2.py
```

Vous devriez voir une sortie similaire à ceci :

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

Remarquez que l'utilisation mémoire a augmenté considérablement par rapport à la méthode précédente de stockage des données sous forme d'une seule chaîne de caractères. Cela s'explique par le fait que chaque ligne de la liste est un objet chaîne de caractères Python distinct, et chaque objet a son propre surcoût mémoire.

## Compréhension de la différence de mémoire

La différence d'utilisation mémoire entre les deux approches montre un concept important en programmation Python appelé surcoût d'objet. Lorsque vous stockez des données sous forme de liste de chaînes de caractères, chaque chaîne est un objet Python distinct. Chaque objet a des exigences mémoire supplémentaires, qui comprennent :

1. L'en-tête de l'objet Python (généralement 16 - 24 octets par objet). Cet en-tête contient des informations sur l'objet, comme son type et son compteur de références.
2. La représentation de la chaîne de caractères elle - même, qui stocke les caractères de la chaîne.
3. Le remplissage d'alignement mémoire. Il s'agit d'un espace supplémentaire ajouté pour garantir que l'adresse mémoire de l'objet est correctement alignée pour un accès efficace.

D'un autre côté, lorsque vous stockez le contenu entier du fichier sous forme d'une seule chaîne de caractères, il n'y a qu'un seul objet, et donc un seul ensemble de surcoûts. Cela le rend plus efficace en termes de mémoire lorsque l'on considère la taille totale des données.

Lors de la conception de programmes qui travaillent avec de grands ensembles de données, vous devez prendre en compte ce compromis entre l'efficacité mémoire et l'accessibilité des données. Parfois, il peut être plus pratique d'accéder aux données lorsqu'elles sont stockées dans une liste de chaînes de caractères, mais cela utilisera plus de mémoire. D'autres fois, vous pourriez privilégier l'efficacité mémoire et choisir de stocker les données sous forme d'une seule chaîne de caractères.
