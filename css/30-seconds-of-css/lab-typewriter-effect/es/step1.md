# Efecto de máquina de escribir

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación con efecto de máquina de escribir, siga estos pasos:

1. Defina dos animaciones, `typing` y `blink`. `typing` anima los caracteres y `blink` anima el cursor.
2. Utilice el pseudo-elemento `::after` para agregar el cursor al elemento contenedor.
3. Utilice JavaScript para establecer el texto para el elemento interno y establecer la variable `--characters`, que contiene la cantidad de caracteres. Esta variable se utiliza para animar el texto.
4. Utilice `white-space: nowrap` y `overflow: hidden` para hacer que el contenido sea invisible según sea necesario.

Aquí está el código HTML:

```html
<div class="typewriter-effect">
  <div class="text" id="typewriter-text"></div>
</div>
```

Y aquí está el código CSS:

```css
.typewriter-effect {
  display: flex;
  justify-content: center;
  font-family: monospace;
}

.typewriter-effect > .text {
  max-width: 0;
  animation: typing 3s steps(var(--characters)) infinite;
  white-space: nowrap;
  overflow: hidden;
}

.typewriter-effect::after {
  content: " |";
  animation: blink 1s infinite;
  animation-timing-function: step-end;
}

@keyframes typing {
  75%,
  100% {
    max-width: calc(var(--characters) * 1ch);
  }
}

@keyframes blink {
  0%,
  75%,
  100% {
    opacity: 1;
  }
  25% {
    opacity: 0;
  }
}
```

Y finalmente, aquí está el código JavaScript:

```js
const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
