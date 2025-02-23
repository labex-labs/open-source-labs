# Masquer les barres de défilement

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour permettre à un élément d'être défilable tout en masquant les barres de défilement, suivez ces étapes :

- Utilisez `overflow: auto` pour activer le défilement sur l'élément.
- Utilisez `scrollbar-width: none` pour masquer les barres de défilement sur Firefox.
- Utilisez `display: none` sur le pseudo-élément `::-webkit-scrollbar` pour masquer les barres de défilement sur les navigateurs WebKit (tels que Chrome, Edge et Safari).

Voici une implémentation d'exemple :

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Masquer les barres de défilement sur les navigateurs WebKit */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
