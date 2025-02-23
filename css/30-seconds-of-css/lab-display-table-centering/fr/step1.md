# Centrage avec display: table

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour centrer un élément enfant à la fois verticalement et horizontalement à l'intérieur de son élément parent, suivez ces étapes :

1. Ajoutez un élément conteneur avec une `height` et une `width` fixes.

```html
<div class="container"></div>
```

2. Ajoutez l'élément enfant à l'intérieur de l'élément conteneur et donnez-lui une classe `.center`.

```html
  <div class="center"><span>Contenu centré</span></div>
</div>
```

3. Dans le CSS, appliquez les styles suivants à l'élément conteneur :

- Fixez `height` et `width` aux valeurs fixes souhaitées.
- Ajoutez une bordure (facultatif).

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. Dans le CSS, appliquez les styles suivants à l'élément enfant :

- Utilisez `display: table` pour faire en sorte que l'élément `.center` se comporte comme un élément `<table>`.
- Fixez `height` et `width` à `100%` pour que l'élément remplisse l'espace disponible à l'intérieur de son élément parent.
- Utilisez `display: table-cell` sur l'élément enfant pour le faire se comporter comme un élément `<td>`.
- Utilisez `text-align: center` et `vertical-align: middle` sur l'élément enfant pour le centrer horizontalement et verticalement.

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
