# Configuración de múltiples respuestas a eventos

Con frecuencia, los elementos de su aplicación se vincularán a múltiples eventos. Si múltiples eventos deben compartir la misma función de manejo, puede proporcionar los tipos de evento como una lista separada por espacios a `.on()`:

```js
// Múltiples eventos, misma función de manejo
$("div").on(
  "click change", // Vincula manejadores para múltiples eventos
  function () {
    console.log("An input was clicked or changed!");
  }
);
```

Cuando cada evento tiene su propio manejador, puede pasar un objeto a `.on()` con uno o más pares clave/valor, donde la clave es el nombre del evento y el valor es la función para manejar el evento.

```js
// Vinculación de múltiples eventos con manejadores diferentes
$("div").on({
  click: function () {
    console.log("clicked!");
  },
  mouseover: function () {
    console.log("hovered!");
  }
});
```

> Puede actualizar la pestaña **Web 8080** para previsualizar la página web.
