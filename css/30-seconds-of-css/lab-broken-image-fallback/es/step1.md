# Alternativa para imágenes que no se cargan

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Cuando una imagen no se carga, muestre un mensaje de error al usuario. Para hacer esto, aplique estilos al elemento `img` como si fuera un contenedor de texto, estableciendo su visualización en bloque y su ancho en 100%. Utilice los pseudo-elementos `::before` y `::after` para mostrar respectivamente el mensaje de error y la URL de la imagen. Estos elementos solo se mostrarán si la imagen no se carga.

A continuación, se muestra un fragmento de código de ejemplo:

```html
<img src="https://nowhere.to.be/found.jpg" />
```

```css
img {
  display: block;
  width: 100%;
  height: auto;
  line-height: 2;
  position: relative;
  text-align: center;
  font-family: sans-serif;
  font-weight: 300;
}

img::before {
  content: "Sorry, this image is unavailable.";
  display: block;
  margin-bottom: 8px;
}

img::after {
  content: "(url: " attr(src) ")";
  display: block;
  font-size: 12px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
