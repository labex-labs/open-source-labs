# Amélioration de la classe Stock

En Python, les classes sont un moyen puissant d'organiser les données et le comportement. Elles nous permettent de regrouper des données et des fonctions liées. Dans cette section, nous allons améliorer notre classe `Stock` en ajoutant une méthode qui affiche les informations sur les actions formatées. C'est un excellent exemple de la façon dont nous pouvons encapsuler à la fois les données et le comportement dans nos classes. L'encapsulation consiste à regrouper les données avec les méthodes qui opèrent sur ces données, ce qui aide à maintenir notre code organisé et plus facile à gérer.

1. Tout d'abord, vous devez ouvrir le fichier `stock.py` dans l'éditeur du WebIDE. Le fichier `stock.py` est l'endroit où nous avons travaillé sur notre classe `Stock`. L'ouvrir dans l'éditeur nous permet de modifier la définition de la classe.

2. Maintenant, nous allons modifier la classe `Stock` pour ajouter une nouvelle méthode `display()`. Cette méthode sera chargée d'imprimer les informations sur les actions de manière bien formatée. Voici comment vous pouvez le faire :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def display(self):
        print(f"Stock: {self.name}, Shares: {self.shares}, Price: ${self.price:.2f}, Total Cost: ${self.cost():.2f}")
```

Dans la méthode `__init__`, nous initialisons le nom de l'action, le nombre de parts et le prix. La méthode `cost` calcule le coût total de l'action en multipliant le nombre de parts par le prix. La nouvelle méthode `display` utilise une f - chaîne pour formater et imprimer les informations sur l'action, y compris le nom, le nombre de parts, le prix et le coût total.

3. Après avoir apporté ces modifications, vous devez enregistrer le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` sur votre clavier ou en cliquant sur l'icône Enregistrer dans l'éditeur. Enregistrer le fichier garantit que vos modifications sont conservées et peuvent être utilisées plus tard.

4. Ensuite, nous allons démarrer une nouvelle session interactive Python. Une session interactive nous permet de tester notre code immédiatement. Pour démarrer la session, exécutez la commande suivante dans le terminal :

```bash
python3 -i stock.py
```

L'option `-i` indique à Python de démarrer une session interactive après avoir exécuté le fichier `stock.py`. De cette façon, nous pouvons utiliser la classe `Stock` et ses méthodes immédiatement.

5. Maintenant, créons un objet d'action et utilisons la nouvelle méthode `display()`. Nous allons créer un objet représentant les actions d'Apple, puis appeler la méthode `display` pour voir les informations formatées. Voici le code :

```python
apple = Stock('AAPL', 200, 154.50)
apple.display()
```

Lorsque vous exécutez ce code dans la session interactive, vous verrez la sortie suivante :

```
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

Cette sortie montre que la méthode `display` fonctionne correctement et formate les informations sur l'action comme prévu.

6. Enfin, créons une liste d'actions et affichons - les toutes. Cela montrera comment nous pouvons utiliser la méthode `display` avec plusieurs objets d'actions. Voici le code :

```python
stocks = [
    Stock('GOOG', 100, 490.10),
    Stock('IBM', 50, 91.50),
    Stock('AAPL', 200, 154.50)
]

for stock in stocks:
    stock.display()
```

Lorsque vous exécutez ce code, vous obtiendrez la sortie suivante :

```
Stock: GOOG, Shares: 100, Price: $490.10, Total Cost: $49010.00
Stock: IBM, Shares: 50, Price: $91.50, Total Cost: $4575.00
Stock: AAPL, Shares: 200, Price: $154.50, Total Cost: $30900.00
```

En ajoutant la méthode `display()` à notre classe, nous avons encapsulé la logique de formatage à l'intérieur de la classe elle - même. Cela rend notre code plus organisé et plus facile à maintenir. Si nous devons changer la façon dont les informations sur les actions sont affichées, nous n'avons qu'à modifier la méthode `display` à un seul endroit, plutôt que d'apporter des modifications dans tout notre code.
