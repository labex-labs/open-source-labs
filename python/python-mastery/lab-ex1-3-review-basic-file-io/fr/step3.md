# Traitement des données

Maintenant que nous avons appris à lire un fichier, l'étape suivante consiste à traiter chaque ligne du fichier pour calculer le coût de chaque achat d'actions. C'est une partie importante du travail avec des données en Python, car cela nous permet d'extraire des informations significatives du fichier.

Chaque ligne du fichier suit un format spécifique : `[Symbole de l'action] [Nombre d'actions] [Prix par action]`. Pour calculer le coût de chaque achat d'actions, nous devons extraire le nombre d'actions et le prix par action de chaque ligne. Ensuite, nous multiplions ces deux valeurs ensemble pour obtenir le coût de cet achat d'actions particulier. Enfin, nous ajoutons ce coût à notre total en cours pour trouver le coût global du portefeuille.

Modifions la fonction `portfolio_cost()` dans le fichier `pcost.py` pour y parvenir. Voici le code modifié :

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

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

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

Analysons étape par étape ce que fait cette fonction modifiée :

1. **Supprime les espaces blancs** : Nous utilisons la méthode `strip()` pour supprimer tout espace blanc en début ou en fin de chaque ligne. Cela garantit que nous n'incluons pas accidentellement des espaces supplémentaires lorsque nous divisons la ligne en champs.
2. **Saute les lignes vides** : Si une ligne est vide (c'est-à-dire qu'elle ne contient que des espaces blancs), nous utilisons l'instruction `continue` pour la sauter. Cela nous aide à éviter les erreurs lors de la tentative de division d'une ligne vide.
3. **Divise la ligne en champs** : Nous utilisons la méthode `split()` pour diviser chaque ligne en une liste de champs en fonction des espaces blancs. Cela nous permet d'accéder à chaque partie de la ligne séparément.
4. **Extrait les données pertinentes** : Nous extrayons le nombre d'actions et le prix par action de la liste de champs. Le nombre d'actions est le deuxième champ, et le prix par action est le troisième champ. Nous convertissons ces valeurs en types de données appropriés (`int` pour le nombre d'actions et `float` pour le prix) afin que nous puissions effectuer des opérations arithmétiques sur elles.
5. **Calcule le coût** : Nous multiplions le nombre d'actions par le prix par action pour calculer le coût de cet achat d'actions.
6. **Ajoute au total** : Nous ajoutons le coût de cet achat d'actions au total en cours.
7. **Affiche des informations de débogage** : Nous affichons des informations sur chaque achat d'actions pour nous aider à voir ce qui se passe. Cela inclut le symbole de l'action, le nombre d'actions, le prix par action et le coût total de l'achat.

Maintenant, exécutons le code pour voir s'il fonctionne. Ouvrez votre terminal et exécutez la commande suivante :

```bash
python3 ~/project/pcost.py
```

Après avoir exécuté la commande, vous devriez voir des informations détaillées sur chaque achat d'actions, suivies du coût total du portefeuille. Cette sortie vous aidera à vérifier que la fonction fonctionne correctement et que vous avez calculé le coût total avec précision.
