# Bouton radio personnalisé

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un bouton radio stylé avec une animation lors du changement d'état, suivez ces étapes :

1. Créez un `.radio-container` en utilisant flexbox pour créer la mise en page appropriée pour les boutons radio.
2. Réinitialisez les styles sur l'élément `<input>` et utilisez-le pour créer le contour et l'arrière-plan du bouton radio.
3. Utilisez l'élément `::before` pour créer le cercle intérieur du bouton radio.
4. Créez un effet d'animation lors du changement d'état en utilisant `transform: scale(1)` et une transition CSS.

Voici un extrait HTML d'exemple :

```html
<div class="radio-container">
  <input class="radio-input" id="apples" type="radio" name="fruit" />
  <label class="radio" for="apples">Apples</label>
  <input class="radio-input" id="oranges" type="radio" name="fruit" />
  <label class="radio" for="oranges">Oranges</label>
</div>
```

Et voici le CSS correspondant :

```css
.radio-container {
  display: flex;
  align-items: center;
}

.radio-container * {
  box-sizing: border-box;
}

.radio-input {
  appearance: none;
  width: 16px;
  height: 16px;
  margin: 0;
  border: 1px solid #cccfdb;
  border-radius: 50%;
  display: grid;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-input::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: scale(0);
  transition: 0.3s transform ease-in-out;
  box-shadow: inset 6px 6px #ffffff;
}

.radio-input:checked {
  background: #0077ff;
  border-color: #0077ff;
}

.radio-input:checked::before {
  transform: scale(1);
}

.radio {
  cursor: pointer;
  padding: 6px 8px;
  margin-right: 6px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
