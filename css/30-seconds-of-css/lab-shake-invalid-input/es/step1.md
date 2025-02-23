# Sacudida en entrada no válida

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación de sacudida cuando hay una entrada no válida, siga estos pasos:

1. Utilice el atributo `pattern` para definir una expresión regular que especifique la entrada permitida. Por ejemplo, use `[A-Za-z]*` para permitir solo letras.
2. Defina una animación de sacudida usando `@keyframes`. Establezca la propiedad `margin-left` para mover la entrada hacia la izquierda y hacia la derecha.
3. Utilice la pseudo-clase `:invalid` para aplicar la animación de sacudida a la entrada.
4. Opcionalmente, agregue una sombra de caja roja a la entrada para indicar el error.

A continuación, se muestra un fragmento de código de ejemplo:

```html
<input type="text" placeholder="Letras solo" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
