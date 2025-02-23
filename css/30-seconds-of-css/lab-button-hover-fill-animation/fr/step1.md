# Animation de remplissage du bouton

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de remplissage au survol, vous pouvez définir les propriétés `couleur` et `background` et appliquer une `transition` appropriée pour animer les changements. Pour déclencher l'animation au survol, utilisez la pseudo-classe `:hover` pour changer les propriétés `background` et `couleur` de l'élément. Voici un extrait de code d'exemple :

```html
<button class="animated-fill-button">Submit</button>
```

```css
.animated-fill-button {
  padding: 20px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  cursor: pointer;
  transition: 0.3s all ease-in-out;
}

.animated-fill-button:hover {
  background: #000;
  color: #fff;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
