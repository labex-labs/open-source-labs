# Centrado con Transformaciones

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para centrar vertical y horizontalmente un elemento hijo dentro de su padre utilizando transformaciones CSS, siga estos pasos:

1. Establezca la propiedad `position` del elemento padre en `relative` y la del elemento hijo en `absolute` para posicionarlo con respecto a su padre.
2. Utilice `left: 50%` y `top: 50%` para desplazar el elemento hijo un 50% desde el borde izquierdo y superior del elemento padre.
3. Utilice `transform: translate(-50%, -50%)` para negar su posición, de modo que quede centrado tanto vertical como horizontalmente.
4. Tenga en cuenta que la `height` y `width` fijas del elemento padre son solo para fines de demostración.

A continuación, se muestra un ejemplo de código HTML:

```html
<div class="parent">
  <div class="child">Contenido centrado</div>
</div>
```

Y aquí está el código CSS correspondiente:

```css
.parent {
  border: 1px solid #9c27b0;
  height: 250px;
  position: relative;
  width: 250px;
}

.child {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
