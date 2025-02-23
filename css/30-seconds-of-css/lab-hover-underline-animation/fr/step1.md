# Animation de soulignement au survol

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet de soulignement animé lorsque l'utilisateur survole le texte, suivez ces étapes :

1. Utilisez `display: inline-block` pour que le soulignement s'étende juste sur la largeur du contenu textuel.
2. Utilisez le pseudo-élément `::after` avec `width: 100%` et `position: absolute` pour le placer sous le contenu.
3. Utilisez `transform: scaleX(0)` pour initialement cacher le pseudo-élément.
4. Utilisez le sélecteur de pseudo-classe `:hover` pour appliquer `transform: scaleX(1)` et afficher le pseudo-élément au survol.
5. Animez `transform` en utilisant `transform-origin: left` et une transition appropriée.
6. Supprimez la propriété `transform-origin` pour que la transformation provienne du centre de l'élément.

Voici un exemple de code HTML pour appliquer l'effet à un élément de texte :

```html
<p class="hover-underline-animation">Survolez ce texte pour voir l'effet!</p>
```

Et voici le code CSS correspondant :

```css
.hover-underline-animation {
  display: inline-block;
  position: relative;
  color: #0087ca;
}

.hover-underline-animation::after {
  content: "";
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #0087ca;
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
