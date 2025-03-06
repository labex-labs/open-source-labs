# Créer la structure HTML

Maintenant que nous comprenons les fichiers de notre projet, créons la structure HTML pour notre motif de damier.

1. Ouvrez à nouveau le fichier `index.html` dans l'éditeur.

2. Nous devons ajouter un élément conteneur pour notre motif de damier. À l'intérieur de la balise `<body>`, remplacez le commentaire par un élément `<div>` qui a une classe "checkerboard" :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Enregistrez le fichier `index.html` en appuyant sur Ctrl+S ou en cliquant sur Fichier > Enregistrer.

4. Maintenant, ajoutons quelques règles CSS de base pour définir les dimensions de notre damier. Ouvrez le fichier `style.css` et ajoutez le code suivant :

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

Ce code CSS effectue les opérations suivantes :

- Définit la largeur et la hauteur de notre damier à 240 pixels
- Définit la couleur de fond sur blanc (#fff)

5. Enregistrez le fichier `style.css`.

6. Actualisez l'onglet **Web 8080** pour voir les modifications.

Vous devriez maintenant voir un carré blanc de 240 pixels de largeur et de hauteur. Ce sera la toile de fond pour notre motif de damier.
