# Création de composants de pipeline de coroutines

Dans cette étape, nous allons créer des coroutines plus spécialisées pour traiter les données boursières. Une coroutine est un type spécial de fonction qui peut suspendre et reprendre son exécution, ce qui est très utile pour construire des pipelines de traitement de données. Chaque coroutine que nous allons créer effectuera une tâche spécifique dans notre pipeline de traitement global.

1. Tout d'abord, vous devez créer un nouveau fichier. Accédez au répertoire `/home/labex/project` et créez un fichier nommé `coticker.py`. Ce fichier contiendra tout le code pour notre traitement de données basé sur les coroutines.

2. Maintenant, commençons à écrire du code dans le fichier `coticker.py`. Nous allons d'abord importer les modules nécessaires et définir la structure de base. Les modules sont des bibliothèques de code pré - écrites qui fournissent des fonctions et des classes utiles. Le code suivant fait exactement cela :

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. Lorsque vous regardez le code ci - dessus, vous remarquerez qu'il y a des erreurs liées à `String()`, `Float()` et `Integer()`. Ce sont des classes que nous devons importer. Nous allons donc ajouter les importations nécessaires en haut du fichier. De cette façon, Python sait où trouver ces classes. Voici le code mis à jour :

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. Ensuite, nous allons ajouter les composants de coroutine qui formeront notre pipeline de traitement de données. Chaque coroutine a une tâche spécifique dans le pipeline. Voici le code pour ajouter ces coroutines :

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. Comprenons ce que chaque coroutine fait :
   - `to_csv` : Son rôle est de convertir les lignes de texte brutes en lignes CSV analysées. C'est important car nos données sont initialement au format texte, et nous devons les diviser en données CSV structurées.
   - `create_ticker` : Cette coroutine prend les lignes CSV et crée des objets `Ticker` à partir d'elles. Les objets `Ticker` représentent les données boursières de manière plus organisée.
   - `negchange` : Elle filtre les objets `Ticker`. Elle ne transmet que les actions dont le prix a diminué. Cela nous permet de nous concentrer sur les actions qui perdent de la valeur.
   - `ticker` : Cette coroutine formate et affiche les données des actions. Elle utilise un formateur pour présenter les données dans un tableau agréable et lisible.

6. Enfin, nous devons ajouter le code du programme principal qui connecte tous ces composants ensemble. Ce code configurera le flux de données à travers le pipeline. Voici le code :

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. Après avoir écrit tout le code, enregistrez le fichier `coticker.py`. Ensuite, ouvrez le terminal et exécutez les commandes suivantes. La commande `cd` change le répertoire pour celui où se trouve notre fichier, et la commande `python3` exécute notre script Python :

```bash
cd /home/labex/project
python3 coticker.py
```

8. Si tout se passe bien, vous devriez voir un tableau formaté dans le terminal. Ce tableau montre les actions dont le prix a diminué. La sortie ressemblera à ceci :

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

Gardez à l'esprit que les valeurs réelles dans le tableau peuvent varier en fonction des données boursières générées.

## Comprendre le flux du pipeline

La partie la plus importante de ce programme est la façon dont les données circulent à travers les coroutines. Découpons - la étape par étape :

1. La fonction `follow` commence par lire les lignes du fichier `stocklog.csv`. C'est notre source de données.
2. Chaque ligne lue est ensuite envoyée à la coroutine `csv_parser`. Le `csv_parser` prend la ligne de texte brute et l'analyse en champs CSV.
3. Les données CSV analysées sont ensuite envoyées à la coroutine `tick_creator`. Cette coroutine crée des objets `Ticker` à partir des lignes CSV.
4. Les objets `Ticker` sont ensuite envoyés à la coroutine `neg_filter`. Cette coroutine vérifie chaque objet `Ticker`. Si le prix de l'action a diminué, elle transmet l'objet ; sinon, elle le rejette.
5. Enfin, les objets `Ticker` filtrés sont envoyés à la coroutine `ticker`. La coroutine `ticker` formate les données et les affiche dans un tableau.

Cette architecture de pipeline est très utile car elle permet à chaque composant de se concentrer sur une seule tâche. Cela rend le code plus modulaire, ce qui signifie qu'il est plus facile à comprendre, à modifier et à maintenir.
