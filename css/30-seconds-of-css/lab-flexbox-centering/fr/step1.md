# Centrage avec Flexbox

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour centrer horizontalement et verticalement un élément enfant à l'intérieur d'un élément parent à l'aide de Flexbox, suivez ces étapes :

1. Créez une disposition Flexbox en définissant la propriété `display` de l'élément parent sur `flex`.
2. Utilisez la propriété `justify-content` pour centrer horizontalement l'enfant en définissant sa valeur sur `center`.
3. Utilisez la propriété `align-items` pour centrer verticalement l'enfant en définissant sa valeur sur `center`.
4. Ajoutez l'élément enfant à l'intérieur de l'élément parent.

Voici un extrait de code d'exemple :

```html
<div class="flexbox-centering">
  <div>Contenu centré.</div>
</div>
```

```css
.flexbox-centering {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
