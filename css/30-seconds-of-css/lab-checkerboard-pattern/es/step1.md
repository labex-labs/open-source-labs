# Patrón de fondo de tablero de ajedrez

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear un patrón de fondo de tablero de ajedrez, sigue estos pasos:

1. Establece la propiedad `background-color` en blanco.
2. Utiliza `background-image` con dos valores de `linear-gradient()`, cada uno con un ángulo diferente para crear el patrón de tablero de ajedrez. Por ejemplo, establece un ángulo en `45deg` y el otro en `-45deg`.
3. Especifica el tamaño del patrón utilizando `background-size`. Por ejemplo, `60px 60px` creará un patrón de 60 por 60 píxeles.
4. Utiliza `background-repeat` para establecer la repetición del patrón. Por ejemplo, `repeat` hará que el patrón se repita en ambas direcciones.
5. Ten en cuenta que las propiedades `height` y `width` del elemento se fijan en 240px con fines de demostración.

Aquí tienes un ejemplo de un elemento HTML con la clase `.checkerboard`:

```html
<div class="checkerboard"></div>
```

Y aquí está el CSS correspondiente:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para previsualizar la página web.
