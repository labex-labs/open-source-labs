# Créer votre propre module

Maintenant que vous savez utiliser les modules existants, il est temps de créer un nouveau module à partir de zéro. Un module en Python est un fichier contenant des définitions et des instructions Python. Il vous permet d'organiser votre code en parties réutilisables et gérables. En créant votre propre module, vous pouvez regrouper les fonctions et les variables liées, rendant votre code plus modulaire et plus facile à maintenir.

## Créer un module de rapport

Créons un simple module pour générer des rapports sur les actions (stocks). Ce module aura des fonctions pour lire un fichier de portefeuille et imprimer un rapport formaté des actions dans le portefeuille.

1. Tout d'abord, nous devons créer un nouveau fichier nommé `report.py`. Pour ce faire, nous utiliserons la ligne de commande. Accédez au répertoire `project` dans votre répertoire personnel et créez le fichier en utilisant la commande `touch`.

```bash
cd ~/project
touch report.py
```

2. Maintenant, ouvrez le fichier `report.py` dans votre éditeur de texte préféré et ajoutez le code suivant. Ce code définit deux fonctions et un bloc principal.

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

La fonction `read_portfolio` lit un fichier contenant des informations sur les actions et retourne une liste de dictionnaires, où chaque dictionnaire représente une action avec les clés `name`, `shares` et `price`. La fonction `print_report` prend un portefeuille (une liste de dictionnaires d'actions) et imprime un rapport formaté montrant le nom de l'action, le nombre de parts, le prix et la valeur totale. Le bloc principal à la fin s'exécute lorsque le fichier est exécuté directement. Il lit le fichier de portefeuille et imprime le rapport.

3. Après avoir ajouté le code, enregistrez et quittez l'éditeur.

## Tester votre module

Testons notre nouveau module pour nous assurer qu'il fonctionne comme prévu.

1. Tout d'abord, nous exécuterons le script directement depuis la ligne de commande. Cela exécutera le bloc principal dans le fichier `report.py`.

```bash
python3 report.py
```

Vous devriez voir un rapport formaté montrant les actions du portefeuille et leurs valeurs. Ce rapport inclut le nom de l'action, le nombre de parts, le prix et la valeur totale, ainsi que la valeur totale de l'ensemble du portefeuille.

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. Ensuite, nous utiliserons le module depuis l'interpréteur Python. Démarrez l'interpréteur Python en exécutant la commande `python3` dans le terminal.

```bash
python3
```

Une fois que l'interpréteur est en cours d'exécution, nous pouvons importer le module `report` et utiliser ses fonctions.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

L'instruction `import report` rend les fonctions et les variables définies dans le fichier `report.py` disponibles dans la session Python actuelle. Nous utilisons ensuite la fonction `read_portfolio` pour lire le fichier de portefeuille et stocker le résultat dans la variable `portfolio`. L'instruction `len(portfolio)` retourne le nombre d'actions dans le portefeuille, et `portfolio[0]` retourne la première action du portefeuille.

Vous devriez voir la sortie suivante :

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. Maintenant, utilisons le module importé pour calculer nous-mêmes le coût total du portefeuille. Nous allons itérer sur les actions du portefeuille et additionner la valeur totale de chaque action.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

La sortie devrait être `44671.15`, qui est la même que la valeur totale imprimée par la fonction `print_report`.

4. Enfin, créons un rapport personnalisé pour un type d'action spécifique. Nous allons filtrer le portefeuille pour inclure seulement les actions IBM, puis utiliser la fonction `print_report` pour imprimer un rapport pour ces actions.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

Cela devrait imprimer un rapport montrant seulement les actions IBM et leurs valeurs.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. Lorsque vous avez terminé les tests, quittez l'interpréteur Python en exécutant la commande `exit()`.

```python
exit()
```

Vous avez maintenant créé et utilisé avec succès votre propre module Python, combinant à la fois des fonctions et un bloc principal qui ne s'exécute que lorsque le fichier est exécuté directement. Cette approche modulaire de la programmation vous permet de réutiliser le code et de rendre vos projets plus organisés et plus faciles à maintenir.
