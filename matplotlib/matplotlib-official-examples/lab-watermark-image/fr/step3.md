# Création d'un graphique de base avec des données aléatoires

Avant d'ajouter notre superposition d'image, nous devons créer un graphique qui servira de base à notre visualisation. Créons un simple diagramme à barres en utilisant des données aléatoires.

1. Créez une nouvelle cellule dans votre notebook et entrez le code suivant :

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

Ce code effectue les opérations suivantes :

- Crée une figure et des axes d'une taille spécifique en utilisant `plt.subplots()`.
- Définit une graine aléatoire pour s'assurer que nous obtenons les mêmes valeurs aléatoires chaque fois que nous exécutons le code.
- Génère 30 valeurs pour l'axe des x (de 0 à 29) et les valeurs correspondantes pour l'axe des y (x plus du bruit aléatoire).
- Crée un diagramme à barres avec des barres vertes en utilisant `ax.bar()`.
- Ajoute des lignes de grille au graphique avec `ax.grid()`.
- Ajoute des étiquettes pour l'axe des x, l'axe des y et un titre pour le graphique.
- Utilise `plt.tight_layout()` pour ajuster l'espacement pour un meilleur aspect.
- Affiche le graphique en utilisant `plt.show()`.

2. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait afficher un diagramme à barres avec des barres vertes représentant les données aléatoires. L'axe des x montre des entiers de 0 à 29, et l'axe des y montre les valeurs correspondantes avec du bruit aléatoire ajouté.

Ce graphique sera la base sur laquelle nous superposerons notre image à l'étape suivante. Remarquez comment nous avons stocké l'objet figure dans la variable `fig` et l'objet axe dans la variable `ax`. Nous aurons besoin de ces variables pour ajouter notre superposition d'image.
