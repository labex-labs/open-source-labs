# Finalisation du programme

Maintenant, nous allons nettoyer notre code et créer la version finale du programme `pcost.py`. Nettoyer le code signifie supprimer toutes les parties inutiles et s'assurer que la sortie est bien formatée. C'est une étape importante en programmation car elle rend notre code plus professionnel et plus facile à comprendre.

Nous commencerons par supprimer les instructions d'impression de débogage. Ces instructions sont utilisées pendant le développement pour vérifier les valeurs des variables et le flux du programme, mais elles ne sont pas nécessaires dans la version finale. Ensuite, nous nous assurerons que la sortie finale est bien formatée.

Voici la version finale du code de `pcost.py` :

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read all lines in the file
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Split the line into fields
                fields = line.split()

                # Extract the relevant data
                # fields[0] is the stock symbol (which we don't need for the calculation)
                shares = int(fields[1])  # Number of shares (second field)
                price = float(fields[2])  # Price per share (third field)

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

Cette version finale du code présente plusieurs améliorations :

1. Gestion des erreurs : Nous avons ajouté du code pour capturer deux types d'erreurs. L'erreur `FileNotFoundError` est levée lorsque le fichier spécifié n'existe pas. Si cela se produit, le programme affichera un message d'erreur et retournera 0,0. Le bloc `Exception` capture toutes les autres erreurs qui pourraient survenir lors du traitement du fichier. Cela rend notre programme plus robuste et moins susceptible de planter de manière inattendue.
2. Formatage approprié : Le coût total est formaté avec deux décimales à l'aide du spécificateur de format `:.2f` dans la chaîne formatée (f-string). Cela rend la sortie plus professionnelle et plus facile à lire.
3. Vérification `__name__ == '__main__'` : C'est un idiome Python courant. Il garantit que le code à l'intérieur du bloc `if` ne s'exécute que lorsque le script est exécuté directement. Si le script est importé comme un module dans un autre script, ce code ne s'exécutera pas. Cela nous donne plus de contrôle sur le comportement de notre script.

Maintenant, exécutons le code final. Ouvrez votre terminal et entrez la commande suivante :

```bash
python3 ~/project/pcost.py
```

Lorsque vous exécutez cette commande, le programme lira le fichier `portfolio.dat`, calculera le coût total du portefeuille et affichera le résultat. Vous devriez voir le coût total du portefeuille, qui devrait être de 44671,15 $.

Félicitations ! Vous avez créé avec succès un programme Python qui lit des données à partir d'un fichier, les traite et calcule un résultat. C'est une grande réussite, et cela montre que vous êtes sur la bonne voie pour devenir un programmeur Python compétent.
