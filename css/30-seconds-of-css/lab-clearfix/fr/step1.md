# Clearfix

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour s'assurer qu'un élément se débarrasse de ses enfants lorsqu'on utilise `float` pour construire des maquettes, vous pouvez utiliser le pseudo-élément `::after` et appliquer `content: ''` pour qu'il puisse affecter la mise en page. En outre, utilisez `clear: both` pour que l'élément efface les flottements gauche et droit précédents. Cependant, cette technique ne fonctionne correctement que si le conteneur n'a pas d'enfants non flottants et s'il n'y a pas de flottements élevés avant le conteneur à nettoyer mais dans le même contexte de formatage (par exemple, des colonnes flottantes). Par exemple :

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

Notez qu'il est recommandé d'utiliser une approche plus moderne, telle que la disposition en boîte flexible (flexbox) ou la disposition en grille, plutôt que d'utiliser `float` pour construire des maquettes.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
