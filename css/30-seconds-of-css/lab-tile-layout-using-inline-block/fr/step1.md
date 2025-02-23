# Disposition en trois carreaux

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une disposition en trois carreaux, utilisez `display: inline-block` au lieu de `float`, `flex` ou `grid`. Utilisez `width` en combinaison avec `calc` pour diviser uniformément la largeur du conteneur en trois colonnes. Pour éviter les espaces blancs, définissez `font-size` sur `0` pour `.tiles` et sur `20px` pour les éléments `<h2>` afin d'afficher le texte. Notez que l'utilisation de `font-size: 0` pour lutter contre les espaces blancs entre les blocs peut entraîner des effets de bord si vous utilisez des unités relatives (par exemple `em`).

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
