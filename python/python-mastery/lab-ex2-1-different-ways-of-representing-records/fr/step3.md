# Travailler avec des données structurées à l'aide de tuples

Jusqu'à présent, nous avons traité du stockage de données textuelles brutes. Mais lorsqu'il s'agit d'analyse de données, nous devons généralement transformer les données en formats plus organisés et structurés. Cela facilite l'exécution de diverses opérations et l'obtention d'informations à partir des données. Dans cette étape, nous allons apprendre à lire les données sous forme de liste de tuples en utilisant le module `csv`. Les tuples sont une structure de données simple et utile en Python qui peut contenir plusieurs valeurs.

## Création d'une fonction de lecture avec des tuples

Créons un nouveau fichier nommé `readrides.py` dans le répertoire `/home/labex/project`. Ce fichier contiendra le code pour lire les données à partir d'un fichier CSV et les stocker sous forme de liste de tuples.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

Ce script définit une fonction appelée `read_rides_as_tuples`. Voici ce qu'elle fait étape par étape :

1. Elle ouvre le fichier CSV spécifié par le paramètre `filename`. Cela nous permet d'accéder aux données à l'intérieur du fichier.
2. Elle utilise le module `csv` pour analyser chaque ligne du fichier. La fonction `csv.reader` nous aide à diviser les lignes en valeurs individuelles.
3. Elle extrait les quatre champs (ligne de bus, date, type de jour et nombre de trajets) de chaque ligne. Ces champs sont importants pour notre analyse de données.
4. Elle convertit le champ 'rides' en entier. Cela est nécessaire car les données dans le fichier CSV sont initialement au format chaîne de caractères, et nous avons besoin d'une valeur numérique pour les calculs.
5. Elle crée un tuple avec ces quatre valeurs. Les tuples sont immuables, ce qui signifie que leurs valeurs ne peuvent pas être modifiées une fois qu'ils sont créés.
6. Elle ajoute le tuple à une liste appelée `records`. Cette liste contiendra tous les enregistrements du fichier CSV.

Maintenant, exécutons le script. Ouvrez votre terminal et entrez la commande suivante :

```bash
python3 /home/labex/project/readrides.py
```

Vous devriez voir une sortie similaire à ceci :

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

Remarquez que l'utilisation mémoire a augmenté par rapport à nos exemples précédents. Voici quelques raisons à cela :

1. Nous stockons maintenant les données dans un format structuré (tuples). Les données structurées nécessitent généralement plus de mémoire car elles ont une organisation définie.
2. Chaque valeur dans le tuple est un objet Python distinct. Les objets Python ont un certain surcoût, ce qui contribue à l'augmentation de l'utilisation mémoire.
3. Nous avons une structure de liste supplémentaire qui contient tous ces tuples. Les listes occupent également de la mémoire pour stocker leurs éléments.

L'avantage d'utiliser cette approche est que nos données sont maintenant correctement structurées et prêtes pour l'analyse. Nous pouvons facilement accéder à des champs spécifiques de chaque enregistrement par index. Par exemple :

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

Cependant, l'accès aux données par index numérique n'est pas toujours intuitif. Il peut être difficile de se souvenir de quel index correspond à quel champ, surtout lorsqu'il y a un grand nombre de champs. Dans l'étape suivante, nous explorerons d'autres structures de données qui peuvent rendre notre code plus lisible et plus maintenable.
