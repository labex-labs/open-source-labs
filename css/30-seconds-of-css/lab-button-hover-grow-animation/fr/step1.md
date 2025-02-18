# Animation d'agrandissement de bouton

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour créer une animation d'agrandissement au survol, vous pouvez utiliser une `transition` appropriée pour animer les changements apportés à l'élément. Utilisez la pseudo-classe `:hover` pour changer la propriété `transform` en `scale(1.1)`. Cela fera grossir l'élément lorsque l'utilisateur le survole.

Voici un exemple de code que vous pouvez utiliser :

```html
<button class="button-grow">Submit</button>
```

```css
.button-grow {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-grow:hover {
  transform: scale(1.1);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
