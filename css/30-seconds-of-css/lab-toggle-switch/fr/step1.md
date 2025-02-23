# Commutateur basculant

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Voici une version plus concise et claire du contenu :

Pour créer un commutateur basculant avec CSS seulement, suivez ces étapes :

1. Associez le `<label>` à l'élément `<input>` de case à cocher en utilisant l'attribut `for`.
2. Utilisez le pseudo-élément `::after` du `<label>` pour créer un bouton rond pour le commutateur.
3. Utilisez le sélecteur de pseudo-classe `:checked` pour changer la position du bouton, en utilisant `transform: translateX(20px)` et la `background-color` du commutateur.
4. Cachez visuellement l'élément `<input>` en utilisant `position: absolute` et `left: -9999px`.

Voici le code HTML :

```html
<input type="checkbox" id="toggle" class="offscreen" />
<label for="toggle" class="switch"></label>
```

Voici le code CSS :

```css
.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  transition: all 0.3s;
}

.switch::after {
  content: "";
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 18px;
  background-color: white;
  top: 1px;
  left: 1px;
  transition: all 0.3s;
}

input[type="checkbox"]:checked + .switch::after {
  transform: translateX(20px);
}

input[type="checkbox"]:checked + .switch {
  background-color: #7983ff;
}

.offscreen {
  position: absolute;
  left: -9999px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
