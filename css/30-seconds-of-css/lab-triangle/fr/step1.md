# Triangle

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une forme triangulaire avec du CSS pur, suivez ces étapes :

1. Utilisez trois bordures avec la même `largeur de bordure` (`20px`) pour créer la forme triangulaire.
2. Définissez la `couleur de bordure` du côté opposé à celui vers lequel pointe le triangle sur la couleur souhaitée. Les bordures adjacentes devraient avoir une `couleur de bordure` de `transparent`.
3. Pour ajuster la taille du triangle, modifiez les valeurs de `largeur de bordure`.

Voici un extrait de code d'exemple :

```html
<div class="triangle"></div>
```

```css
.triangle {
  width: 0;
  height: 0;
  border-top: 20px solid #9c27b0;
  border-left: 20px solid transparent;
  border-right: 20px solid transparent;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
