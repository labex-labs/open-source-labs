# Lecture d'un portefeuille à partir d'un fichier CSV

Dans cette étape, nous allons créer une fonction qui lit les données d'actions à partir d'un fichier CSV et renvoie une liste d'objets `Stock`. Un objet `Stock` représente une participation en actions, et à la fin de cette étape, vous pourrez lire un portefeuille d'actions à partir d'un fichier CSV.

## Comprendre les fichiers CSV

CSV, qui signifie Comma-Separated Values (valeurs séparées par des virgules), est un format très courant pour stocker des données tabulaires. Imaginez-le comme une feuille de calcul simple. Chaque ligne dans un fichier CSV représente une ligne de données, et les colonnes au sein de cette ligne sont séparées par des virgules. Habituellement, la première ligne d'un fichier CSV contient les en-têtes. Ces en-têtes décrivent le type de données présent dans chaque colonne. Par exemple, dans un fichier CSV de portefeuille d'actions, les en-têtes pourraient être "Name", "Shares" et "Price".

## Instructions d'implémentation

1. Tout d'abord, ouvrez le fichier `stock.py` dans votre éditeur de code. S'il est déjà ouvert, c'est parfait ! Sinon, trouvez-le et ouvrez-le. C'est là que nous allons ajouter notre nouvelle fonction.

2. Une fois le fichier `stock.py` ouvert, recherchez le commentaire `# TODO: Add read_portfolio(filename) function here`. Ce commentaire est un emplacement qui nous indique où placer notre nouvelle fonction.

3. En dessous de ce commentaire, ajoutez la fonction suivante. Cette fonction s'appelle `read_portfolio`, et elle prend un nom de fichier en argument. Le but de cette fonction est de lire le fichier CSV, extraire les données d'actions et créer une liste d'objets `Stock`.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Analysons ce que fait cette fonction. Tout d'abord, elle crée une liste vide appelée `portfolio`. Ensuite, elle ouvre le fichier CSV en mode lecture. L'instruction `next(f)` saute la première ligne, qui est la ligne d'en-tête. Après cela, elle parcourt chaque ligne du fichier. Pour chaque ligne, elle divise la ligne en une liste de valeurs, extrait le nom, le nombre d'actions et le prix, crée un objet `Stock` et l'ajoute à la liste `portfolio`. Enfin, elle renvoie la liste `portfolio`.

4. Après avoir ajouté la fonction, enregistrez le fichier `stock.py`. Vous pouvez le faire en appuyant sur `Ctrl+S` sur votre clavier ou en sélectionnant "File > Save" dans le menu de votre éditeur de code. Enregistrer le fichier garantit que vos modifications sont conservées.

5. Maintenant, nous devons tester notre fonction `read_portfolio`. Créez un nouveau script Python appelé `test_portfolio.py`. Ce script importera la fonction `read_portfolio` à partir du fichier `stock.py`, lira le portefeuille à partir d'un fichier CSV et affichera des informations sur chaque action du portefeuille.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

Dans ce script, nous importons d'abord la fonction `read_portfolio`. Ensuite, nous appelons la fonction avec le nom de fichier `portfolio.csv` pour obtenir la liste d'objets `Stock`. Après cela, nous parcourons la liste et affichons des informations sur chaque action. Enfin, nous affichons le nombre total d'actions dans le portefeuille.

6. Pour exécuter le script de test, ouvrez votre terminal ou invite de commande, naviguez jusqu'au répertoire où se trouve le fichier `test_portfolio.py` et exécutez la commande suivante :

```bash
python3 test_portfolio.py
```

Si tout fonctionne correctement, vous devriez voir une sortie qui liste toutes les actions du fichier `portfolio.csv`, ainsi que leurs noms, le nombre d'actions et les prix. Vous devriez également voir le nombre total d'actions dans le portefeuille.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $00.44

Total number of stocks in portfolio: 7
```

Cette sortie confirme que votre fonction `read_portfolio` lit correctement le fichier CSV et crée des objets `Stock` à partir de ses données.
