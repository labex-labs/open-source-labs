# Patrón de fondo de puntos de lunares

`index.html` y `style.css` ya se han proporcionado en la máquina virtual (VM).

Para crear un patrón de fondo de puntos de lunares, puedes seguir estos pasos:

1. Establece la propiedad `background-color` en negro.
2. Utiliza la propiedad `background-image` con dos valores de `radial-gradient()` para crear dos puntos.
3. Especifica el tamaño del patrón utilizando la propiedad `background-size`. Utiliza `background-position` para colocar adecuadamente los dos gradientes.
4. Establece `background-repeat` en `repeat`.
5. Ten en cuenta que la altura (`height`) y el ancho (`width`) fijos del elemento son solo con fines de demostración.

A continuación, se muestra un ejemplo de código HTML para un elemento div con la clase `polka-dot`:

```html
<div class="polka-dot"></div>
```

Y aquí está el código CSS correspondiente:

```css
.polka-dot {
  width: 240px;
  height: 240px;
  background-color: #000;
  background-image:
    radial-gradient(#fff 10%, transparent 11%),
    radial-gradient(#fff 10%, transparent 11%);
  background-size: 60px 60px;
  background-position:
    0 0,
    30px 30px;
  background-repeat: repeat;
}
```

Haz clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puedes actualizar la pestaña **Web 8080** para ver una vista previa de la página web.
