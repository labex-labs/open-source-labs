# Diseño de tres bloques

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un diseño de tres bloques, utiliza `display: inline-block` en lugar de `float`, `flex` o `grid`. Utiliza `width` en combinación con `calc` para dividir uniformemente el ancho del contenedor en tres columnas. Para evitar espacios en blanco, establece `font-size` en `0` para `.tiles` y en `20px` para los elementos `<h2>` para mostrar el texto. Tenga en cuenta que utilizar `font-size: 0` para combatir los espacios en blanco entre bloques puede causar efectos secundarios si se utilizan unidades relativas (por ejemplo, `em`).

```html
<div class="tiles">
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
  <div class="tile">
    <img src="https://via.placeholder.com/200x150" />
    <h2>30 Seconds of CSS</h2>
  </div>
</div>
```

```css
.tiles {
  width: 600px;
  font-size: 0;
  margin: 0 auto;
}

.tile {
  width: calc(600px / 3);
  display: inline-block;
}

.tile h2 {
  font-size: 20px;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
