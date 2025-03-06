# Traçage de base avec position de titre par défaut

Dans cette étape, vous allez créer un simple graphique linéaire et ajouter un titre centré, qui est la position par défaut dans Matplotlib.

## Création d'un cahier Jupyter

Une fois le démarrage de la machine virtuelle (VM) terminé, cliquez dans le coin supérieur gauche pour basculer vers l'onglet **Notebook** et accéder à Jupyter Notebook.

![click-notebook](https://file.labex.io/images/click-notebook.png)

Vous devrez peut-être attendre quelques secondes que Jupyter Notebook finisse de charger. En raison des limitations de Jupyter Notebook, la validation des opérations ne peut pas être automatisée.

Si vous rencontrez des problèmes pendant le laboratoire, n'hésitez pas à demander de l'aide à Labby. Veuillez fournir des commentaires après la session afin que nous puissions résoudre rapidement tout problème.

## Importation de Matplotlib

Maintenant, commençons par importer la bibliothèque Matplotlib. Dans la première cellule de votre cahier, tapez le code suivant et exécutez - le en appuyant sur Shift+Enter :

```python
import matplotlib.pyplot as plt
```

Cela importe le module pyplot de Matplotlib et lui attribue l'alias `plt`, qui est une convention courante.

## Création d'un graphique simple

Ensuite, créons un graphique linéaire de base. Dans une nouvelle cellule, entrez le code suivant et exécutez - le :

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

Vous devriez voir un simple graphique linéaire avec des valeurs de 0 à 9 affichées dans la sortie.

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## Ajout d'un titre par défaut (centré)

Maintenant, ajoutons un titre à notre graphique. La position par défaut d'un titre est centrée en haut du graphique. Dans une nouvelle cellule, entrez le code suivant :

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

Exécutez la cellule, et vous devriez voir le graphique avec un titre centré en haut.

La fonction `title()` sans aucun paramètre supplémentaire placera le titre au centre, qui est la position par défaut.
