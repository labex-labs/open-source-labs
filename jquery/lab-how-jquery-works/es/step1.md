# Cómo funciona jQuery

> `index.html` ya se ha proporcionado en la VM.

Este archivo se generará automáticamente durante la inicialización del entorno. Si no se genera automáticamente, cree el archivo y funcione como se muestra en la imagen anterior. El código de la función es el siguiente:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Aquí va tu código.
    </script>
  </body>
</html>
```

El atributo `src` en el elemento `<script>` debe apuntar a una copia de jQuery. Descargue una copia de jQuery desde la página [Descargando jQuery](https://jquery.com/download/) y guarde el archivo `jquery.min.js` en el mismo directorio que su archivo HTML.

> Nota: Cuando descargue jQuery, el nombre del archivo puede contener un número de versión, por ejemplo, `jquery-x.y.z.js`. Asegúrese de renombrar este archivo a `jquery.js` o actualizar el atributo `src` del elemento `<script>` para que coincida con el nombre del archivo.

#### Lanzando código cuando el documento está listo

Para asegurarse de que su código se ejecute después de que el navegador termine de cargar el documento, muchos programadores de JavaScript envuelven su código en una función `onload`:

```js
window.onload = function () {
  alert("welcome");
};
```

Lamentablemente, el código no se ejecuta hasta que todas las imágenes hayan terminado de descargarse, incluyendo los anuncios publicitarios. Para ejecutar el código tan pronto como el documento esté listo para ser manipulado, jQuery tiene una declaración conocida como el [evento ready](http://api.jquery.com/ready/):

```js
$(document).ready(function () {
  // Aquí va tu código.
});
```

> Nota: La biblioteca jQuery expone sus métodos y propiedades a través de dos propiedades del objeto `window` llamadas `jQuery` y `$`. `$` es simplemente un alias para `jQuery` y a menudo se utiliza porque es más corto y rápido de escribir.

Por ejemplo, dentro del evento ready, puede agregar un controlador de clic al enlace:

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

Copie el código jQuery anterior en su archivo HTML donde dice `// Aquí va tu código`. Luego, guarde su archivo HTML y recargue la página de prueba en su navegador.

#### Ejemplo completo

El siguiente ejemplo ilustra el código de control de clic discutido anteriormente, incrustado directamente en el `<body>` HTML. Tenga en cuenta que en la práctica, por lo general, es mejor colocar su código en un archivo JS separado y cargarlo en la página con el atributo `src` de un elemento `<script>`.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>hágame clic</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
