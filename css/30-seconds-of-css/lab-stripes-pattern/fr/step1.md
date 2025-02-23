# Motif de fond à rayures

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Ce code crée un motif de rayures verticales sur un fond blanc.

Pour créer le motif :

- Définissez la propriété `background-color` sur blanc.
- Utilisez `background-image` avec une valeur `linear-gradient()` pour créer une rayure verticale.
- Définissez la propriété `background-size` pour spécifier la taille de chaque rayure.
- Définissez `background-repeat` sur `repeat` pour permettre au motif de remplir l'élément.

Notez que la largeur et la hauteur fixes de l'élément sont uniquement à des fins de démonstration.

Voici un extrait de code d'exemple :

```html
<div class="stripes"></div>
```

```css
.stripes {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(90deg, transparent 50%, #000 50%);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
