# Botón de Hamburguesa

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un menú de hamburguesa que transicione a un botón de cruz al pasar el cursor, siga estos pasos:

1. Utilice un contenedor `div` con la clase `.hamburger-menu` que contenga las barras superior, inferior y del medio.
2. Establezca el contenedor en `display: flex` con `flex-flow: column wrap`.
3. Agregue distancia entre las barras utilizando `justify-content: space-between`.
4. Utilice `transform: rotate()` para rotar las barras superior e inferior en 45 grados y `opacity: 0` para desvanecer la barra del medio al pasar el cursor.
5. Utilice `transform-origin: left` para que las barras giren alrededor del punto izquierdo.

A continuación, se muestra el código HTML correspondiente:

```html
<div class="hamburger-menu">
  <div class="bar top"></div>
  <div class="bar middle"></div>
  <div class="bar bottom"></div>
</div>
```

Y aquí está el código CSS:

```css
.hamburger-menu {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  height: 2.5rem;
  width: 2.5rem;
  cursor: pointer;
}

.hamburger-menu.bar {
  height: 5px;
  background: black;
  border-radius: 5px;
  margin: 3px 0px;
  transform-origin: left;
  transition: all 0.5s;
}

.hamburger-menu:hover.top {
  transform: rotate(45deg);
}

.hamburger-menu:hover.middle {
  opacity: 0;
}

.hamburger-menu:hover.bottom {
  transform: rotate(-45deg);
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
