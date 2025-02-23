# Image Rotate on Hover

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet de rotation pour une image au survol, utilisez les propriétés `scale()`, `rotate()` et `transition` lorsque vous survolez l'élément parent, qui devrait être un élément `<figure>`. Pour vous assurer que la transformation de l'image ne déborde pas de l'élément parent, ajoutez `overflow: hidden` à la feuille de style CSS de l'élément parent. Voici un exemple de code HTML et CSS :

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
