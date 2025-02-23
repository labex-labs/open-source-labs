# Vollbild

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Element im Vollbildmodus zu gestalten, können Sie den CSS-Pseudo-Element-Selektor `:fullscreen` verwenden. Sie können auch einen Button erstellen, der das Element für die Vorschau in den Vollbildmodus versetzt, indem Sie einen `<button>` und `Element.requestFullscreen()` verwenden. Hier ist ein Beispielcode:

```html
<div class="container">
  <p>
    <em
      >Klicken Sie auf den Button unten, um das Element in den Vollbildmodus zu
      versetzen.
    </em>
  </p>
  <div class="element" id="element">
    <p>Ich ändere die Farbe im Vollbildmodus!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    Gehe in den Vollbildmodus!
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

/* Für Internet Explorer */
.element:-ms-fullscreen p {
  sichtbarkeit: sichtbar;
}

/* Für moderne Browser */
.element:fullscreen {
  hintergrundfarbe: #e4708a;
  breite: 100vw;
  höhe: 100vh;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite zu Vorschauen.
