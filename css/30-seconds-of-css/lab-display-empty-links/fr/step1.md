# Style Links With No Text

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour afficher l'URL du lien pour les liens qui n'ont pas de texte, vous pouvez utiliser la pseudo-classe `:empty` pour sélectionner de tels liens, la pseudo-classe `:not` pour exclure les liens avec du texte, et la propriété `content` en combinaison avec la fonction `attr()` pour afficher l'URL du lien dans le pseudo-élément `::before`. Voici un extrait de code d'exemple :

```html
<a href="https://30secondsofcode.org"></a>
```

```css
a[href^="http"]:empty::before {
  content: attr(href);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
