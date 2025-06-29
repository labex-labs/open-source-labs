# Création de la classe Ticker

Dans le traitement de données, travailler avec des données brutes peut être assez difficile. Pour organiser et optimiser notre travail avec les données d'actions, nous allons définir une classe appropriée pour représenter les cours d'actions. Cette classe servira de modèle pour nos données d'actions, rendant notre pipeline de traitement de données plus robuste et plus facile à gérer.

## Création du fichier ticker.py

1. Tout d'abord, nous devons créer un nouveau fichier dans le WebIDE. Vous pouvez le faire en cliquant sur l'icône "New File" ou en cliquant avec le bouton droit dans l'explorateur de fichiers et en sélectionnant "New File". Nommez ce fichier `ticker.py`. Ce fichier contiendra le code de notre classe `Ticker`.

2. Maintenant, ajoutons le code suivant à votre fichier `ticker.py` nouvellement créé. Ce code définira notre classe `Ticker` et configurera un simple pipeline de traitement pour la tester.

```python
# ticker.py

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

if __name__ == '__main__':
    from follow import follow
    import csv
    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    for record in records:
        print(record)
```

3. Après avoir ajouté le code, enregistrez le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` ou en sélectionnant "File" → "Save" dans le menu. Enregistrer le fichier garantit que vos modifications sont conservées et peuvent être exécutées plus tard.

## Compréhension du code

Examinons de plus près ce que ce code fait étape par étape :

1. Au début du code, nous importons `Structure` et les types de champs du module `structure.py`. Ce module a déjà été configuré pour vous. Ces importations sont essentielles car elles fournissent les éléments de base pour notre classe `Ticker`. La classe `Structure` sera la classe de base de notre classe `Ticker`, et les types de champs comme `String`, `Float` et `Integer` définiront les types de données de nos champs de données d'actions.

2. Ensuite, nous définissons une classe `Ticker` qui hérite de `Structure`. Cette classe a plusieurs champs qui représentent différents aspects des données d'actions :
   - `name` : Ce champ stocke le symbole de l'action, comme "IBM" ou "AAPL". Il nous aide à identifier de quelle société d'actions nous traitons.
   - `price` : Il contient le prix actuel de l'action. C'est une information cruciale pour les investisseurs.
   - `date` et `time` : Ces champs nous indiquent quand le cours de l'action a été généré. Savoir l'heure et la date est important pour analyser les tendances des prix des actions au fil du temps.
   - `change` : Cela représente la variation du prix de l'action. Il montre si le prix de l'action a augmenté ou diminué par rapport à un point précédent.
   - `open`, `high`, `low` : Ces champs représentent le prix d'ouverture, le prix le plus élevé et le prix le plus bas de l'action pendant une certaine période. Ils nous donnent une idée de la fourchette de prix de l'action.
   - `volume` : Ce champ stocke le nombre d'actions échangées. Un volume d'échange élevé peut indiquer un fort intérêt du marché pour une action particulière.

3. Dans le bloc `if __name__ == '__main__':`, nous configurons un pipeline de traitement. Ce bloc de code sera exécuté lorsque nous exécutons directement le fichier `ticker.py`.
   - `follow('stocklog.csv')` est une fonction qui génère des lignes à partir du fichier `stocklog.csv`. Elle nous permet de lire le fichier ligne par ligne.
   - `csv.reader(lines)` prend ces lignes et les analyse en données de ligne. CSV (Comma - Separated Values) est un format de fichier courant pour stocker des données tabulaires, et cette fonction nous aide à extraire les données de chaque ligne.
   - `(Ticker.from_row(row) for row in rows)` est une expression générateur. Elle prend chaque ligne de données et la convertit en un objet `Ticker`. De cette façon, nous transformons les données CSV brutes en objets structurés plus faciles à manipuler.
   - La boucle `for` itère sur ces objets `Ticker` et les affiche un par un. Cela nous permet de voir les données structurées en action.

## Exécution du code

Exécutons le code pour voir comment il fonctionne :

1. Tout d'abord, nous devons nous assurer que nous sommes dans le répertoire du projet dans le terminal. Si vous n'y êtes pas déjà, utilisez la commande suivante pour y accéder :

   ```bash
   cd /home/labex/project
   ```

2. Une fois que vous êtes dans le bon répertoire, exécutez le script `ticker.py` en utilisant la commande suivante :

   ```bash
   python3 ticker.py
   ```

3. Après avoir exécuté le script, vous devriez voir une sortie similaire à ceci (vos données varieront) :
   ```
   Ticker(IBM, 103.53, 6/11/2007, 09:53.59, 0.46, 102.87, 103.53, 102.77, 541633)
   Ticker(MSFT, 30.21, 6/11/2007, 09:54.01, 0.16, 30.05, 30.21, 29.95, 7562516)
   Ticker(AA, 40.01, 6/11/2007, 09:54.01, 0.35, 39.67, 40.15, 39.31, 576619)
   Ticker(T, 40.1, 6/11/2007, 09:54.08, -0.16, 40.2, 40.19, 39.87, 1312959)
   ```

Vous pouvez arrêter l'exécution du script en appuyant sur `Ctrl+C` une fois que vous avez vu assez de résultats.

Remarquez comment les données CSV brutes ont été transformées en objets `Ticker` structurés. Cette transformation rend les données beaucoup plus faciles à manipuler dans notre pipeline de traitement, car nous pouvons maintenant accéder et manipuler les données d'actions en utilisant les champs définis dans la classe `Ticker`.
