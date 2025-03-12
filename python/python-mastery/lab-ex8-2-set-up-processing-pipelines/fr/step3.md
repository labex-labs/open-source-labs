# Construction d'un pipeline de données plus complexe

Maintenant, nous allons faire passer notre pipeline de données au niveau supérieur en ajoutant des filtres et en améliorant la présentation des données. Cela facilitera l'analyse et la compréhension des informations avec lesquelles nous travaillons. Nous allons apporter des modifications à notre script `ticker.py`. Le filtrage des données nous aidera à nous concentrer sur les informations spécifiques qui nous intéressent, et la présentation des données dans un tableau bien formaté les rendra plus lisibles.

## Mise à jour du fichier ticker.py

1. Tout d'abord, ouvrez votre fichier `ticker.py` dans le WebIDE. Le WebIDE est un outil qui vous permet d'écrire et d'éditer du code directement dans votre navigateur. Il offre un environnement pratique pour apporter des modifications à vos scripts Python.

2. Ensuite, nous devons remplacer le bloc `if __name__ == '__main__':` dans le fichier `ticker.py` par le code suivant. Ce bloc de code est le point d'entrée de notre script, et en le remplaçant, nous allons modifier la façon dont le script traite et affiche les données.

```python
if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name', 'price', 'change'], formatter)
```

3. Après avoir apporté ces modifications, enregistrez le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` sur votre clavier ou en sélectionnant "File" → "Save" dans le menu. Enregistrer le fichier garantit que vos modifications sont conservées et peuvent être exécutées plus tard.

## Compréhension du pipeline amélioré

Examinons de plus près ce que fait ce pipeline amélioré. Comprendre chaque étape vous aidera à voir comment les différentes parties du code travaillent ensemble pour traiter et afficher les données.

1. Nous commençons par importer `create_formatter` et `print_table` du module `tableformat`. Ce module est déjà configuré pour vous, et il fournit des fonctions qui nous aident à formater et à afficher les données dans un joli tableau.

2. Ensuite, nous créons un formateur de texte en utilisant `create_formatter('text')`. Ce formateur sera utilisé pour formater les données d'une manière facile à lire.

3. Maintenant, décomposons le pipeline étape par étape :
   - `follow('stocklog.csv')` est une fonction qui génère des lignes à partir du fichier `stocklog.csv`. Elle surveille en continu le fichier pour détecter de nouvelles données et fournit les lignes une par une.
   - `csv.reader(lines)` prend les lignes générées par `follow` et les analyse en données de ligne. Cela est nécessaire car les données dans le fichier CSV sont au format texte, et nous devons les convertir en un format structuré avec lequel nous pouvons travailler.
   - `(Ticker.from_row(row) for row in rows)` est une expression générateur qui convertit chaque ligne de données en un objet `Ticker`. Un objet `Ticker` représente une action et contient des informations telles que le nom de l'action, le prix et la variation.
   - `(rec for rec in records if rec.change < 0)` est une autre expression générateur qui filtre les objets `Ticker`. Elle ne conserve que les objets où la variation du prix de l'action est négative. Cela nous permet de nous concentrer sur les actions dont le prix a diminué.
   - `print_table(negative, ['name', 'price', 'change'], formatter)` prend les objets `Ticker` filtrés et les formate en un tableau en utilisant le formateur que nous avons créé précédemment. Il affiche ensuite le tableau dans la console.

Ce pipeline démontre la puissance des générateurs. Au lieu de charger toutes les données du fichier en mémoire d'un coup, nous enchaînons plusieurs opérations (lecture, analyse, conversion, filtrage) et traitons les données un élément à la fois. Cela économise de la mémoire et rend le code plus efficace.

## Exécution du pipeline amélioré

Exécutons le code mis à jour pour voir les résultats.

1. Tout d'abord, assurez - vous que vous êtes dans le répertoire du projet dans le terminal. Si vous n'y êtes pas déjà, vous pouvez y accéder en utilisant la commande suivante :

   ```bash
   cd /home/labex/project
   ```

2. Une fois que vous êtes dans le répertoire du projet, exécutez le script `ticker.py` en utilisant la commande suivante :

   ```bash
   python3 ticker.py
   ```

3. Après avoir exécuté le script, vous devriez voir un tableau bien formaté dans le terminal. Ce tableau montre uniquement les actions avec des variations de prix négatives.

   ```
          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19
   ```

Si vous avez vu assez de résultats et que vous souhaitez arrêter l'exécution du script, vous pouvez appuyer sur `Ctrl+C` sur votre clavier.

## La puissance des pipelines de générateurs

Ce que nous avons créé ici est un puissant pipeline de traitement de données. Résumons ce qu'il fait :

1. Il surveille en continu le fichier `stocklog.csv` pour détecter de nouvelles données. Cela signifie que lorsque de nouvelles données sont ajoutées au fichier, le pipeline les traitera automatiquement.
2. Il analyse les données CSV du fichier en objets `Ticker` structurés. Cela facilite le travail avec les données et l'exécution d'opérations sur elles.
3. Il filtre les données en fonction de critères spécifiques, dans ce cas, les variations de prix négatives. Cela nous permet de nous concentrer sur les actions qui perdent de la valeur.
4. Il formate et présente les données filtrées dans un tableau lisible. Cela facilite l'analyse des données et la formulation de conclusions.

L'un des principaux avantages de l'utilisation de générateurs dans ce pipeline est qu'il utilise un minimum de mémoire. Les générateurs produisent des valeurs à la demande, ce qui signifie qu'ils ne stockent pas toutes les données en mémoire d'un coup. Cela est similaire aux pipes Unix, où chaque composant traite les données et les transmet au composant suivant.

Vous pouvez considérer les générateurs comme des blocs Lego. Tout comme vous pouvez empiler des blocs Lego pour créer différentes structures, vous pouvez combiner des générateurs pour créer des flux de travail de traitement de données puissants. Cette approche modulaire vous permet de construire des systèmes complexes à partir de composants simples et réutilisables.
