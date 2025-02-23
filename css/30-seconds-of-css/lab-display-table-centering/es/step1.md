# Centrado con Display Table

`index.html` y `style.css` ya se han proporcionado en la VM.

Para centrar un elemento hijo tanto vertical como horizontalmente dentro de su elemento padre, siga estos pasos:

1. Agregue un elemento contenedor con un `height` y `width` fijos.

```html
<div class="container"></div>
```

2. Agregue el elemento hijo dentro del elemento contenedor y asígnale una clase de `.center`.

```html
  <div class="center"><span>Contenido centrado</span></div>
</div>
```

3. En el CSS, aplique los siguientes estilos al elemento contenedor:

- Establezca `height` y `width` en los valores fijos deseados.
- Agregue un borde (opcional).

```css
.container {
  border: 1px solid #9c27b0;
  height: 250px;
  width: 250px;
}
```

4. En el CSS, aplique los siguientes estilos al elemento hijo:

- Utilice `display: table` para hacer que el elemento `.center` se comporte como un elemento `<table>`.
- Establezca `height` y `width` en `100%` para hacer que el elemento ocupe todo el espacio disponible dentro de su elemento padre.
- Utilice `display: table-cell` en el elemento hijo para que se comporte como un elemento `<td>`.
- Utilice `text-align: center` y `vertical-align: middle` en el elemento hijo para centrarlo horizontal y verticalmente.

```css
.center {
  display: table;
  height: 100%;
  width: 100%;
}

.center > span {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
