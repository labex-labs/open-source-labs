# Cercle

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une forme circulaire à l'aide de CSS pur, utilisez la propriété `border-radius: 50%` pour courber les bords de l'élément. Assurez-vous de définir à la fois `width` et `height` sur la même valeur pour obtenir un cercle parfait. Si des valeurs différentes sont utilisées, une ellipse sera créée à la place. Voici un extrait de code d'exemple :

```html
<div class="circle"></div>
```

```css
.circle {
  border-radius: 50%;
  width: 32px;
  height: 32px;
  background: #9c27b0;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
