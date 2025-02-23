# Transform Centering

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour centrer verticalement et horizontalement un élément enfant à l'intérieur de son parent à l'aide de transformations CSS, suivez ces étapes :

1. Définissez la propriété `position` de l'élément parent sur `relative` et celle de l'élément enfant sur `absolute` pour le positionner par rapport à son parent.
2. Utilisez `left: 50%` et `top: 50%` pour déplacer l'élément enfant de 50% du bord gauche et supérieur de l'élément parent.
3. Utilisez `transform: translate(-50%, -50%)` pour annuler sa position, de sorte qu'il soit centré verticalement et horizontalement.
4. Notez que la hauteur et la largeur fixes de l'élément parent sont uniquement à des fins de démonstration.

Voici un exemple de code HTML :

```html
<div class="parent">
  <div class="child">Contenu centré</div>
</div>
```

Et voici le code CSS correspondant :

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
