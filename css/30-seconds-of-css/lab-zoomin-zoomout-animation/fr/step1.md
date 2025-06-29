# Comprendre la structure HTML

Avant de commencer à créer notre animation, nous devons comprendre la structure HTML avec laquelle nous allons travailler. Dans cette étape, nous examinerons le fichier HTML fourni et apporterons les modifications nécessaires.

1. Ouvrez le fichier `index.html` dans l'éditeur.

2. Si le fichier est vide ou manquant, créez - le avec le contenu suivant :

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Comprenons ce que fait ce HTML :
   - Nous avons une structure de document HTML standard avec un titre et des paramètres de vue (viewport)
   - Nous établissons un lien vers un fichier CSS externe nommé `style.css`
   - Nous incluons un en - tête et un paragraphe pour expliquer notre démonstration
   - Plus important encore, nous avons un élément `<div>` avec la classe `zoom - in - out - box` qui sera animé

4. Enregistrez le fichier `index.html` si vous avez apporté des modifications.

Cet élément div sera notre toile de fond pour créer l'animation. Dans l'étape suivante, nous allons styliser cet élément à l'aide de CSS.
