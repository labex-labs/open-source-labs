# Animación de contracción de botón

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear una animación de contracción al pasar el cursor sobre un elemento, puedes utilizar una propiedad `transition` adecuada para animar los cambios y la pseudo-clase `:hover` para desencadenar la animación. Por ejemplo, si quieres que un botón con la clase `button-shrink` se contraiga cuando un usuario pasa el cursor sobre él, puedes agregar el siguiente CSS:

```css
.button-shrink {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.button-shrink:hover {
  transform: scale(0.8);
}
```

Esto aplicará un efecto de transición a todas las propiedades del botón cuando haya un cambio, y cuando el usuario pase el cursor sobre él, el botón se contraerá al 80% de su tamaño original. El código HTML para el botón es el siguiente:

```html
<button class="button-shrink">Submit</button>
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
