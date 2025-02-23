# Truncar texto de varias líneas

`index.html` y `style.css` ya se han proporcionado en la VM.

Para truncar texto que tiene más de una línea, siga estos pasos:

1. Utilice `overflow: hidden` para evitar que el texto desborde sus dimensiones.
2. Establezca un ancho fijo de `400px` para garantizar que el elemento tenga al menos una dimensión constante.
3. Establezca `height: 109.2px` según se calculó a partir del `font-size`, utilizando la fórmula `font-size * line-height * numberOfLines` (en este caso `26 * 1.4 * 3 = 109.2`).
4. Agregue la clase `truncate-text-multiline` al elemento `p` en su HTML.
5. Establezca `font-size: 26px` y `line-height: 1.4` en el CSS para la clase `.truncate-text-multiline`.
6. Establezca `color: #333` y `background: #f5f6f9` para dar estilo al texto.
7. Para crear un degradado desde `transparent` hasta el `background-color`, agregue las siguientes reglas CSS al pseudo-elemento `.truncate-text-multiline::after`:

```css
.truncate-text-multiline::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 150px;
  height: 36.4px;
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #f5f6f9 50%);
}
```

Esto creará un contenedor de degradado con una altura de `36.4px`, calculada para el contenedor de degradado, basada en la fórmula `font-size * line-height` (en este caso `26 * 1.4 = 36.4`). El pseudo-elemento `::after` se coloca en la esquina inferior derecha del elemento `.truncate-text-multiline`.

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
