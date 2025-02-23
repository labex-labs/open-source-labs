# Plein écran

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour styliser un élément en mode plein écran, vous pouvez utiliser le sélecteur de pseudo-élément CSS `:fullscreen`. Vous pouvez également créer un bouton qui met l'élément en plein écran à des fins de prévisualisation à l'aide d'un `<button>` et de `Element.requestFullscreen()`. Voici un exemple de code :

```html
<div class="container">
  <p>
    <em
      >Cliquez sur le bouton ci-dessous pour mettre l'élément en mode plein
      écran.
    </em>
  </p>
  <div class="element" id="element">
    <p>Je change de couleur en mode plein écran!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    Passer en plein écran!
  </button>
</div>
```

```css
.container {
  margin: 40px auto;
  max-width: 700px;
}

.element {
  padding: 20px;
  height: 300px;
  width: 100%;
  background-color: skyblue;
  box-sizing: border-box;
}

.element p {
  text-align: center;
  color: white;
  font-size: 3em;
}

/* Pour Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* Pour les navigateurs modernes */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
