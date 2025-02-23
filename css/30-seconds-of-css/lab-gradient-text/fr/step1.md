# Texte en gradient

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour donner à un texte une couleur en gradient, vous pouvez utiliser des propriétés CSS. Tout d'abord, utilisez la propriété `background` avec une valeur `linear-gradient()` pour donner à l'élément de texte un fond en gradient. Ensuite, utilisez `webkit-text-fill-color: transparent` pour remplir le texte avec une couleur transparente. Enfin, utilisez `webkit-background-clip: text` pour découper le fond avec le texte et remplir le texte avec le fond en gradient comme couleur. Voici un extrait de code d'exemple :

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
