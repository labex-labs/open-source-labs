# Algo Después de que una Animación Finalice

Un error común al implementar efectos de jQuery es suponer que la ejecución del siguiente método en tu cadena esperará hasta que la animación termine de ejecutarse.

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

Es importante entender que `.fadeIn()` arriba solo inicia la animación. Una vez iniciada, la animación se implementa cambiando rápidamente las propiedades CSS en un bucle `setInterval()` de JavaScript. Cuando llamas a `.fadeIn()`, inicia el bucle de animación y luego devuelve el objeto jQuery, pasándolo a `.addClass() `que luego agregará la clase de estilo `lookAtMe` mientras el bucle de animación acaba de comenzar.

Para diferir una acción hasta después de que una animación haya terminado de ejecutarse, necesitas usar una función de devolución de llamada de animación. Puedes especificar tu devolución de llamada de animación como el segundo argumento pasado a cualquiera de los métodos de animación discutidos anteriormente. Para el fragmento de código anterior, podemos implementar una devolución de llamada de la siguiente manera:

```js
// Desvanecer hacia dentro todos los párrafos ocultos; luego agregue una clase de estilo a ellos (correcto con devolución de llamada de animación)
$("div.hidden").fadeIn(1500, function () {
  // this = elemento DOM que acaba de terminar de ser animado
  $(this).addClass("lookAtMe");
});
```

Tenga en cuenta que puede usar la palabra clave this para hacer referencia al elemento DOM que está siendo animado. También tenga en cuenta que la devolución de llamada se llamará para cada elemento en el objeto jQuery. Esto significa que si tu selector no devuelve ningún elemento, tu devolución de llamada de animación nunca se ejecutará! Puedes resolver este problema probando si tu selección devolvió algún elemento; si no es así, puedes simplemente ejecutar la devolución de llamada inmediatamente.

```js
// Ejecute una devolución de llamada incluso si no hubo elementos para animar
var someElement = $("#nonexistent");

var cb = function () {
  console.log("hecho!");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> Puedes actualizar la pestaña **Web 8080** para previsualizar la página web.
