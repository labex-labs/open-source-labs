# Comprender la estructura HTML

Antes de comenzar a crear nuestra animación, necesitamos entender la estructura HTML con la que trabajaremos. En este paso, examinaremos el archivo HTML proporcionado y realizaremos las modificaciones necesarias.

1. Abre el archivo `index.html` en el editor.

2. Si el archivo está vacío o falta, créalo con el siguiente contenido:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. Entendamos qué hace este HTML:

   - Tenemos una estructura de documento HTML estándar con un título y configuraciones de viewport (área visible)
   - Enlazamos a un archivo CSS externo llamado `style.css`
   - Incluimos un encabezado y un párrafo para explicar nuestra demostración
   - Lo más importante, tenemos un elemento `<div>` con la clase `zoom-in-out-box` que se animará

4. Guarda el archivo `index.html` si hiciste algún cambio.

Este elemento div será nuestro lienzo para crear la animación. En el siguiente paso, estilizaremos este elemento utilizando CSS.
