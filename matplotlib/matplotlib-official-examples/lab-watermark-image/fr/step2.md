# Chargement et examen de l'image

Maintenant que nous avons importé nos bibliothèques, nous devons charger l'image que nous souhaitons superposer sur notre graphique. Matplotlib propose quelques images d'exemple que nous pouvons utiliser pour pratiquer.

1. Créez une nouvelle cellule dans votre notebook et entrez le code suivant :

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

Ce code effectue les opérations suivantes :

- Utilise `cbook.get_sample_data()` pour charger une image d'exemple nommée 'logo2.png' depuis la collection de données d'exemple de Matplotlib.
- Utilise `image.imread()` pour lire le fichier image dans un tableau NumPy.
- Affiche des informations sur les dimensions et le type de données de l'image.
- Crée une figure et affiche l'image à l'aide de `plt.imshow()`.
- Masque les graduations et les étiquettes de l'axe avec `plt.axis('off')`.
- Ajoute un titre à la figure.
- Affiche la figure à l'aide de `plt.show()`.

2. Exécutez la cellule en appuyant sur Shift+Enter.

La sortie devrait afficher des informations sur l'image et montrer le logo de Matplotlib. La forme de l'image indique les dimensions de l'image (hauteur, largeur, canaux de couleur), et le type de données nous indique comment les données de l'image sont stockées.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

Cette étape est importante car elle nous aide à comprendre l'image que nous utiliserons comme superposition. Nous pouvons voir son apparence et ses dimensions, ce qui sera utile pour décider comment la positionner sur notre graphique.
