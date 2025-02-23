# Ajuster une image à l'intérieur d'un conteneur

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour ajuster une image à l'intérieur de son conteneur tout en conservant son rapport de largeur à hauteur, vous pouvez utiliser `object-fit: contain`. Pour remplir le conteneur avec l'image tout en conservant son rapport de largeur à hauteur, utilisez `object-fit: cover`. Si vous voulez positionner l'image au centre du conteneur, vous pouvez utiliser `object-position: center`.

Voici un exemple de manière dont vous pouvez utiliser ces propriétés :

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

Et le CSS correspondant :

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
