# Borde con triángulo superior

`index.html` y `style.css` ya se han proporcionado en la VM.

Para crear un contenedor de contenido con un triángulo en la parte superior, siga estos pasos:

1. Utilice los pseudo-elementos `::before` y `::after` para crear dos triángulos.
2. Establezca el `border-color` y el `background-color` de los triángulos para que coincidan con el contenedor.
3. Establezca el `border-width` del triángulo `::before` para que sea `1px` más ancho que el triángulo `::after` para que actúe como borde.
4. Coloque el triángulo `::after` `1px` a la derecha del triángulo `::before` para que se muestre el borde izquierdo.

A continuación, se muestra un ejemplo de código HTML para el contenedor:

```html
<div class="container">Border with top triangle</div>
```

Y aquí está el código CSS correspondiente:

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
