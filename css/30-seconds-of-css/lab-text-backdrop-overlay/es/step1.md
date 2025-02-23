# Superposición de texto en imágenes

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para mostrar texto sobre una imagen con una superposición, utiliza la propiedad `backdrop-filter` para aplicar un efecto de `desenfoque(14px)` y `brillo(80%)`. Esto garantiza que el texto sea legible independientemente de la imagen de fondo y el color. Aquí hay un ejemplo de código HTML:

```html
<div>
  <h3 class="text-overlay">Hello, World</h3>
  <img src="https://picsum.photos/id/1050/1200/800" />
</div>
```

Y el código CSS correspondiente:

```css
div {
  position: relative;
}

.text-overlay {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 300;
  color: white;
  backdrop-filter: blur(14px) brightness(80%);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
