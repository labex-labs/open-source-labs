# Imagen que gira al pasar el cursor

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un efecto de rotación para una imagen al pasar el cursor, utiliza las propiedades `scale()`, `rotate()` y `transition` al pasar el cursor sobre el elemento padre, que debe ser un elemento `<figure>`. Para garantizar que la transformación de la imagen no desborde del elemento padre, agrega `overflow: hidden` a la hoja de estilos del elemento padre. Aquí hay un ejemplo de código HTML y CSS:

```html
<figure class="hover-rotate">
  <img src="https://picsum.photos/id/669/600/800.jpg" />
</figure>
```

```css
.hover-rotate {
  overflow: hidden;
  margin: 8px;
  min-width: 240px;
  max-width: 320px;
  width: 100%;
}

.hover-rotate img {
  transition: all 0.3s;
  box-sizing: border-box;
  max-width: 100%;
}

.hover-rotate:hover img {
  transform: scale(1.3) rotate(5deg);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
