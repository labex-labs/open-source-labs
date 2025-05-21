# Crear la estructura HTML

Ahora que comprendemos los archivos de nuestro proyecto, creemos la estructura HTML para nuestro patrón de tablero de ajedrez.

1. Abre nuevamente el archivo `index.html` en el editor.

2. Necesitamos agregar un elemento contenedor para nuestro patrón de tablero de ajedrez. Dentro de la etiqueta `<body>`, reemplaza el comentario con un elemento `<div>` que tenga una clase de "checkerboard":

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Guarda el archivo `index.html` presionando Ctrl+S o haciendo clic en Archivo > Guardar.

4. Ahora, agreguemos algunos estilos CSS básicos para definir las dimensiones de nuestro tablero de ajedrez. Abre el archivo `style.css` y agrega el siguiente código:

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

Este código CSS hace lo siguiente:

- Establece el ancho y la altura de nuestro tablero de ajedrez en 240 píxeles.
- Establece el color de fondo en blanco (#fff).

5. Guarda el archivo `style.css`.

6. Refresca la pestaña **Web 8080** para ver los cambios.

Ahora deberías ver un cuadrado blanco con un ancho y una altura de 240 píxeles. Este será el lienzo para nuestro patrón de tablero de ajedrez.
