# Sibling Fade

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour faire s'estomper les frères et sœurs d'un élément survolé :

1. Animer les changements d'opacité en utilisant la propriété `transition`.

```css
span {
  padding: 0 16px;
  transition: opacity 0.3s;
}
```

2. Changer l'opacité de tous les éléments sauf celui survolé par la souris à `0,5` en utilisant les sélecteurs pseudo-classes `:hover` et `:not`.

```css
.sibling-fade:hover span:not(:hover) {
  opacity: 0.5;
}
```

Voici un exemple de code HTML :

```html
<div class="sibling-fade">
  <span>Item 1</span> <span>Item 2</span> <span>Item 3</span>
  <span>Item 4</span> <span>Item 5</span> <span>Item 6</span>
</div>
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
