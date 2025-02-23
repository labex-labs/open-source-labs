# Tronquer le texte

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour tronquer le texte qui est plus long qu'une ligne et ajouter un ellipse à la fin, utilisez les propriétés CSS suivantes :

- `overflow: hidden` pour empêcher le texte de déborder de ses dimensions
- `white-space: nowrap` pour empêcher le texte de dépasser une ligne en hauteur
- `text-overflow: ellipsis` pour ajouter un ellipse si le texte dépasse ses dimensions
- Spécifiez une largeur fixe (`width`) pour l'élément pour savoir quand afficher un ellipse

Notez que cette méthode ne fonctionne que pour les éléments d'une seule ligne. Par exemple :

```html
<p class="truncate-text">If I exceed one line's width, I will be truncated.</p>
```

```css
.truncate-text {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 200px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
