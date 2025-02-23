# Sélection de texte personnalisée

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour modifier le style du texte sélectionné, utilisez le pseudo-sélecteur `::selection`. Voici un extrait de code d'exemple pour sélectionner et styliser le texte à l'intérieur d'un élément de paragraphe :

```html
<p class="custom-text-selection">Sélectionnez un peu de ce texte.</p>
```

```css
::selection {
  background: aquamarine;
  color: black;
}

.custom-text-selection::selection {
  background: deeppink;
  color: white;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
