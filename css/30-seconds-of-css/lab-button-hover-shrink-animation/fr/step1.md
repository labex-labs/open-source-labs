# Animation de rétrécissement de bouton

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une animation de rétrécissement au survol d'un élément, vous pouvez utiliser une propriété `transition` appropriée pour animer les changements et la pseudo-classe `:hover` pour déclencher l'animation. Par exemple, si vous voulez rétrécir un bouton avec la classe `button-shrink` lorsque l'utilisateur le survole, vous pouvez ajouter le CSS suivant :

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

Cela appliquera un effet de transition à toutes les propriétés du bouton lorsqu'il y a un changement, et lorsque l'utilisateur le survole, le bouton se rétrécira à 80 % de sa taille d'origine. Le code HTML pour le bouton est le suivant :

```html
<button class="button-shrink">Submit</button>
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
