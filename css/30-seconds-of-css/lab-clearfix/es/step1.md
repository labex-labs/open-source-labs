# Clearfix

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para garantizar que un elemento se limpie a sí mismo de sus hijos al utilizar `float` para construir diseños, puedes utilizar el pseudo-elemento `::after` y aplicar `content: ''` para permitir que afecte al diseño. Además, utiliza `clear: both` para que el elemento elimine los flotados tanto hacia la izquierda como hacia la derecha. Sin embargo, esta técnica solo funciona correctamente si no hay hijos no flotados en el contenedor y no hay flotados altos antes del contenedor con clearfix pero en el mismo contexto de formato (por ejemplo, columnas flotadas). Por ejemplo:

```html
<div class="clearfix">
  <div class="floated">float a</div>
  <div class="floated">float b</div>
  <div class="floated">float c</div>
</div>
```

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.floated {
  float: left;
  padding: 4px;
}
```

Tenga en cuenta que se recomienda utilizar un enfoque más moderno, como el diseño con flexbox o grid, en lugar de utilizar `float` para construir diseños.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
