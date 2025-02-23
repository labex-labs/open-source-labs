# Désactiver la sélection

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour rendre le contenu d'un élément non sélectionnable, ajoutez la propriété CSS `user-select: none` au sélecteur. Cependant, cette méthode n'est pas entièrement sécurisée pour empêcher les utilisateurs de copier le contenu.

Exemple :

```html
<p>Vous pouvez me sélectionner.</p>
<p class="unselectable">Vous ne pouvez pas me sélectionner!</p>
```

```css
.unselectable {
  user-select: none;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
