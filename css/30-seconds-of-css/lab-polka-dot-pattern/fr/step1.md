# Motif de fond en points de polka

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour créer un motif de fond en points de polka, vous pouvez suivre ces étapes :

1. Définissez la propriété `background-color` sur noir.
2. Utilisez la propriété `background-image` avec deux valeurs `radial-gradient()` pour créer deux points.
3. Spécifiez la taille du motif à l'aide de la propriété `background-size`. Utilisez `background-position` pour placer correctement les deux dégradés.
4. Définissez `background-repeat` sur `repeat`.
5. Notez que la hauteur (`height`) et la largeur (`width`) fixes de l'élément sont uniquement à des fins de démonstration.

Voici un exemple de code HTML pour un élément div avec la classe `polka-dot` :

```html
<div class="polka-dot"></div>
```

Et voici le code CSS correspondant :

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
