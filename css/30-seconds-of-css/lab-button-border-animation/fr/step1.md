# Animation de bordure de bouton

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de bordure au survol, vous pouvez utiliser les pseudo-éléments `::before` et `::after` pour générer deux boîtes de `24px` de largeur positionnées au-dessus et en-dessous de la boîte. Ensuite, appliquez la pseudo-classe `:hover` pour augmenter la `largeur` de ces éléments à `100%` au survol et animer la transition à l'aide de `transition`.

Voici un extrait de code d'exemple :

```html
<button class="animated-border-button">Submit</button>
```

```css
.animated-border-button {
  background-color: #263059;
  border: none;
  color: #ffffff;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
}

.animated-border-button::before,
.animated-border-button::after {
  border: 0 solid transparent;
  transition: all 0.3s;
  content: "";
  height: 0;
  position: absolute;
  width: 24px;
}

.animated-border-button::before {
  border-top: 2px solid #263059;
  right: 0;
  top: -4px;
}

.animated-border-button::after {
  border-bottom: 2px solid #263059;
  bottom: -4px;
  left: 0;
}

.animated-border-button:hover::before,
.animated-border-button:hover::after {
  width: 100%;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
