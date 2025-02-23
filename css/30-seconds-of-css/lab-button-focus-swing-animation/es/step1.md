# Animación de balanceo del botón

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear una animación de balanceo al enfocar, debes usar una `transición` adecuada para animar los cambios en el elemento. Luego, aplica la pseudo-clase `:focus` al elemento y utiliza `animation` con `transform` para que oscile. Finalmente, agrega `animation-iteration-count` para reproducir la animación solo una vez. Aquí hay un ejemplo de cómo hacer esto en HTML y CSS:

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
