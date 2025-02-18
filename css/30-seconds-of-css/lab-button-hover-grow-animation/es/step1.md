# Animación de crecimiento de botón

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear una animación de crecimiento al pasar el cursor sobre un elemento, puedes utilizar una `transition` adecuada para animar los cambios en el elemento. Utiliza la pseudo-clase `:hover` para cambiar la propiedad `transform` a `scale(1.1)`. Esto hará que el elemento crezca cuando el usuario pase el cursor sobre él.

A continuación, se muestra un ejemplo de fragmento de código que puedes utilizar:

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

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
