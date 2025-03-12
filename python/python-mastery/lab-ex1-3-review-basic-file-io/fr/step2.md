# Ouvrir et lire un fichier

Dans cette étape, nous allons apprendre à ouvrir et lire un fichier en Python. L'entrée/sortie de fichiers (E/S) est un concept fondamental en programmation. Elle permet à votre programme d'interagir avec des fichiers externes, comme des fichiers texte, des fichiers CSV, etc. En Python, l'une des méthodes les plus courantes pour travailler avec des fichiers consiste à utiliser la fonction `open()`.

La fonction `open()` est utilisée pour ouvrir un fichier en Python. Elle prend deux arguments importants. Le premier argument est le nom du fichier que vous souhaitez ouvrir. Le deuxième argument est le mode dans lequel vous souhaitez ouvrir le fichier. Lorsque vous souhaitez lire un fichier, vous utilisez le mode 'r'. Cela indique à Python que vous ne souhaitez que lire le contenu du fichier sans apporter de modifications.

Maintenant, ajoutons un peu de code au fichier `pcost.py` pour ouvrir et lire le fichier `portfolio.dat`. Ouvrez le fichier `pcost.py` dans votre éditeur de code et ajoutez le code suivant :

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

Analysons ce que ce code fait :

1. Tout d'abord, nous définissons une fonction nommée `portfolio_cost()`. Cette fonction prend un nom de fichier en tant que paramètre d'entrée. Le but de cette fonction est de calculer le coût total d'un portefeuille d'actions en fonction des données du fichier.
2. À l'intérieur de la fonction, nous utilisons la fonction `open()` pour ouvrir le fichier spécifié en mode lecture. L'instruction `with` est utilisée ici pour garantir que le fichier est correctement fermé une fois que nous avons terminé de le lire. C'est une bonne pratique pour éviter les fuites de ressources.
3. Nous utilisons ensuite une boucle `for` pour lire le fichier ligne par ligne. Pour chaque ligne du fichier, nous l'affichons. Cela ne sert qu'à des fins de débogage, afin que nous puissions voir quelles données nous lisons à partir du fichier.
4. Après avoir lu le fichier, la fonction retourne le coût total. Actuellement, le coût total est fixé à 0,0 car nous n'avons pas encore implémenté le calcul réel.
5. En dehors de la fonction, nous appelons la fonction `portfolio_cost()` avec le nom de fichier 'portfolio.dat'. Cela signifie que nous demandons à la fonction de calculer le coût total en fonction des données du fichier `portfolio.dat`.
6. Enfin, nous affichons le coût total à l'aide d'une chaîne formatée (f-string).

Maintenant, exécutons ce code pour voir ce qu'il fait. Vous pouvez exécuter le fichier Python depuis le terminal en utilisant la commande suivante :

```bash
python3 ~/project/pcost.py
```

Lorsque vous exécutez cette commande, vous devriez voir chaque ligne du fichier `portfolio.dat` affichée sur le terminal, suivie du coût total, qui est actuellement fixé à 0,0. Cette sortie vous permet de vérifier que le fichier est correctement lu.
