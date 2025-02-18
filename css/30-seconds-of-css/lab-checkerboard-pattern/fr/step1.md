# Motif de fond en damier

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour créer un motif de fond en damier, suivez ces étapes :

1. Définissez la propriété `background-color` sur blanc.
2. Utilisez `background-image` avec deux valeurs `linear-gradient()`, chacune avec un angle différent pour créer le motif de damier. Par exemple, définissez un angle à `45deg` et l'autre à `-45deg`.
3. Spécifiez la taille du motif en utilisant `background-size`. Par exemple, `60px 60px` créera un motif de 60 pixels sur 60 pixels.
4. Utilisez `background-repeat` pour définir la répétition du motif. Par exemple, `repeat` fera répéter le motif dans les deux directions.
5. Notez que les propriétés `height` et `width` de l'élément sont fixées à 240px à des fins de démonstration.

Voici un exemple d'élément HTML avec la classe `.checkerboard` :

```html
<div class="checkerboard"></div>
```

Et voici le CSS correspondant :

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
