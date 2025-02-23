# Superposition de texte sur une image

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour afficher du texte au-dessus d'une image avec une superposition, utilisez la propriété `backdrop-filter` pour appliquer un effet `blur(14px)` et `brightness(80%)`. Cela garantit que le texte est lisible quelle que soit l'image et la couleur d'arrière-plan. Voici un exemple de code HTML :

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

Et le code CSS correspondant :

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
