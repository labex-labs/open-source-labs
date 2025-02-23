# Centrage de grille

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour centrer un élément enfant horizontalement et verticalement à l'intérieur d'un élément parent, suivez ces étapes :

1. Créez une mise en page en grille en utilisant `display: grid`.
2. Utilisez `justify-content: center` pour centrer l'enfant horizontalement.
3. Utilisez `align-items: center` pour centrer l'enfant verticalement.

Voici une structure HTML d'exemple :

```html
<div class="parent">
  <div class="child">Contenu centré.</div>
</div>
```

Et le CSS correspondant :

```css
.parent {
  display: grid;
  justify-content: center;
  align-items: center;
  height: 100px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
