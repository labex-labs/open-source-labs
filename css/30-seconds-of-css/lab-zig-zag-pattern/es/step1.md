# Patrón de fondo en zigzag

`index.html` y `style.css` ya se han proporcionado en la máquina virtual.

Para crear un patrón de fondo en zigzag, siga los siguientes pasos:

1. Establezca un fondo blanco utilizando `background-color`.
2. Cree las partes de un patrón en zigzag utilizando `background-image` con cuatro valores de `linear-gradient()`.
3. Especifique el tamaño del patrón utilizando `background-size`.
4. Coloque las partes del patrón en las ubicaciones correctas utilizando `background-position`.
5. Para repetir el patrón, utilice `background-repeat`.
6. **Nota:** La `altura` y el `ancho` del elemento se fijan solo con fines de demostración.

A continuación, se muestra un fragmento de código de ejemplo:

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%),
    linear-gradient(315deg, #000 25%, transparent 25%),
    linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
