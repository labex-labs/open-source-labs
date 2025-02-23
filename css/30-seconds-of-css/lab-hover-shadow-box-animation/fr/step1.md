# Animation de boîte à ombre au survol

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une boîte à ombre autour du texte lorsqu'il est survolé, suivez ces étapes :

1. Définissez `transform: perspective(1px)` pour donner à l'élément un espace 3D en affectant la distance entre le plan Z et l'utilisateur, et `translateZ(0)` pour repositioner l'élément `p` le long de l'axe z dans l'espace 3D.
2. Utilisez `box-shadow` pour rendre la boîte transparente.
3. Activez les transitions pour `box-shadow` et `transform` en utilisant la propriété `transition-property`.
4. Appliquez une nouvelle `box-shadow` et `transform: scale(1.2)` pour modifier l'échelle du texte en utilisant les sélecteurs pseudo-classes `:hover`, `:active` et `:focus`.
5. Ajoutez la classe `hover-shadow-box-animation` à l'élément `p`.

Voici le code HTML :

```html
<p class="hover-shadow-box-animation">Box it!</p>
```

Et voici le code CSS :

```css
.hover-shadow-box-animation {
  display: inline-block;
  vertical-align: middle;
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px transparent;
  margin: 10px;
  transition:
    box-shadow 0.3s,
    transform 0.3s;
}

.hover-shadow-box-animation:hover,
.hover-shadow-box-animation:focus,
.hover-shadow-box-animation:active {
  box-shadow: 1px 10px 10px -10px rgba(0, 0, 24, 0.5);
  transform: scale(1.2);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
