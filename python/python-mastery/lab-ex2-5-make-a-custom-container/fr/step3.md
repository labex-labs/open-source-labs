# Optimisation de la mémoire avec des données organisées par colonnes

Dans le stockage de données traditionnel, nous stockons souvent chaque enregistrement sous forme de dictionnaire distinct, ce qui est appelé une approche orientée ligne. Cependant, cette méthode peut consommer une quantité importante de mémoire. Une autre façon de procéder consiste à stocker les données par colonnes. Dans l'approche orientée colonne, nous créons des listes distinctes pour chaque attribut, et chaque liste contient toutes les valeurs de cet attribut spécifique. Cela peut nous aider à économiser de la mémoire.

1. Tout d'abord, vous devez créer un nouveau fichier Python dans votre répertoire de projet. Ce fichier contiendra le code pour lire les données de manière orientée colonne. Nommez le fichier `readrides.py`. Vous pouvez utiliser les commandes suivantes dans le terminal pour y parvenir :

```bash
cd ~/project
touch readrides.py
```

La commande `cd ~/project` change le répertoire courant en votre répertoire de projet, et la commande `touch readrides.py` crée un nouveau fichier vide nommé `readrides.py`.

2. Ensuite, ouvrez le fichier `readrides.py` dans l'éditeur WebIDE. Ensuite, ajoutez le code Python suivant au fichier. Ce code définit une fonction `read_rides_as_columns` qui lit les données de trajets en bus à partir d'un fichier CSV et les stocke dans quatre listes distinctes, chacune représentant une colonne de données.

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

Dans ce code, nous importons d'abord les modules nécessaires `csv`, `sys` et `tracemalloc`. Le module `csv` est utilisé pour lire les fichiers CSV, `sys` peut être utilisé pour des opérations liées au système (bien qu'il ne soit pas utilisé dans cette fonction), et `tracemalloc` est utilisé pour le profilage de mémoire. À l'intérieur de la fonction, nous initialisons quatre listes vides pour stocker les différentes colonnes de données. Ensuite, nous ouvrons le fichier, sautons la ligne d'en-tête et parcourons chaque ligne du fichier, ajoutant les valeurs correspondantes aux listes appropriées. Enfin, nous renvoyons un dictionnaire contenant ces quatre listes.

3. Maintenant, analysons pourquoi l'approche orientée colonne peut économiser de la mémoire. Nous le ferons dans le shell Python. Exécutez le code suivant :

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

Dans ce code, nous importons d'abord le module `readrides` que nous venons de créer et le module `tracemalloc`. Ensuite, nous estimons l'utilisation de mémoire pour l'approche orientée ligne. Nous supposons que chaque dictionnaire a une surcharge de 240 octets, et nous multiplions cela par le nombre de lignes dans le fichier original pour obtenir l'utilisation totale de mémoire pour les données orientées ligne. Pour l'approche orientée colonne, nous supposons que sur un système 64 bits, chaque pointeur prend 8 octets. Étant donné que nous avons 4 colonnes et un pointeur par entrée, nous calculons l'utilisation totale de mémoire pour les données orientées colonne. Enfin, nous calculons les économies de mémoire en soustrayant l'utilisation de mémoire orientée colonne de l'utilisation de mémoire orientée ligne.

Ce calcul montre que l'approche orientée colonne devrait économiser environ 120 Mo de mémoire par rapport à l'approche orientée ligne avec des dictionnaires.

4. Vérifions cela en mesurant l'utilisation réelle de mémoire avec le module `tracemalloc`. Exécutez le code suivant :

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

Dans ce code, nous commençons d'abord à suivre l'utilisation de mémoire en utilisant `tracemalloc.start()`. Ensuite, nous appelons la fonction `read_rides_as_columns` pour lire les données à partir du fichier `ctabus.csv`. Après cela, nous utilisons `tracemalloc.get_traced_memory()` pour obtenir l'utilisation actuelle et maximale de mémoire. Enfin, nous arrêtons de suivre l'utilisation de mémoire en utilisant `tracemalloc.stop()`.

La sortie vous montrera l'utilisation réelle de mémoire de votre structure de données orientée colonne. Cela devrait être nettement inférieur à notre estimation théorique pour l'approche orientée ligne.

Les économies de mémoire significatives proviennent de l'élimination de la surcharge de milliers d'objets dictionnaire. Chaque dictionnaire en Python a une surcharge fixe, quelle que soit le nombre d'éléments qu'il contient. En utilisant un stockage orienté colonne, nous n'avons besoin que de quelques listes au lieu de milliers de dictionnaires.
