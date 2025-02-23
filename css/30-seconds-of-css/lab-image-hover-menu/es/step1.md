# Menú al pasar el cursor sobre una imagen

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para mostrar una superposición de menú cuando el usuario pasa el cursor sobre una imagen, use una `<figure>` para envolver el elemento `<img>` y un elemento `<div>` que contendrá los enlaces del menú. Aplique las siguientes propiedades CSS para animar la imagen al pasar el cursor, creando un efecto de deslizamiento:

- `opacidad`
- `derecha`
  Establezca el atributo `left` del `<div>` en el negativo del ancho del elemento. Restablezcalo a `0` cuando pase el cursor sobre el elemento padre para deslizar el menú hacia adentro. Finalmente, use `display: flex`, `flex-direction: column` y `justify-content: center` en el `<div>` para centrar verticalmente los elementos del menú.

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Inicio</a>
    <a href="#">Precios</a>
    <a href="#">Acerca de</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
