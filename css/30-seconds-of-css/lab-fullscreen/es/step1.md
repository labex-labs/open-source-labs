# Pantalla Completa

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para dar estilo a un elemento en modo pantalla completa, puedes usar el selector de pseudo-elemento CSS `:fullscreen`. También puedes crear un botón que ponga el elemento en pantalla completa con fines de vista previa usando un `<button>` y `Element.requestFullscreen()`. Aquí hay un ejemplo de código:

```html
<div class="container">
  <p>
    <em
      >Haz clic en el botón siguiente para poner el elemento en modo pantalla
      completa.
    </em>
  </p>
  <div class="element" id="element">
    <p>Cambio de color en modo pantalla completa!</p>
  </div>
  <br />
  <button
    onclick="var el = document.getElementById('element'); el.requestFullscreen();"
  >
    ¡Entrar en Pantalla Completa!
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

/* Para Internet Explorer */
.element:-ms-fullscreen p {
  visibility: visible;
}

/* Para navegadores modernos */
.element:fullscreen {
  background-color: #e4708a;
  width: 100vw;
  height: 100vh;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
