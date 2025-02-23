# Input With Prefix

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une entrée avec un préfixe visuel non modifiable, suivez ces étapes :

1. Utilisez `display: flex` pour créer un élément conteneur avec la classe `.input-box`.
2. Supprimez la bordure et la mise en surbrillance du champ `<input>` et appliquez-les à l'élément parent à la place pour le rendre ressemblant à une zone de saisie.
3. Utilisez le sélecteur de pseudo-classe `:focus-within` pour styliser l'élément parent en conséquence lorsque l'utilisateur interagit avec le champ `<input>`.

Voici le code HTML :

```html
<div class="input-box">
  <span class="prefix">+30</span>
  <input type="tel" placeholder="210 123 4567" />
</div>
```

Et voici le code CSS :

```css
.input-box {
  display: flex;
  align-items: center;
  max-width: 300px;
  background: #fff;
  border: 1px solid #a0a0a0;
  border-radius: 4px;
  padding-left: 0.5rem;
  overflow: hidden;
  font-family: sans-serif;
}

.input-box.prefix {
  font-weight: 300;
  font-size: 14px;
  color: #999;
}

.input-box input {
  flex-grow: 1;
  font-size: 14px;
  background: #fff;
  border: none;
  outline: none;
  padding: 0.5rem;
}

.input-box:focus-within {
  border-color: #777;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
