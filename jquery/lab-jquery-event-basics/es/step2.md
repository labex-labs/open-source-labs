# Extendiendo eventos a nuevos elementos de página

Es importante tener en cuenta que `.on()` solo puede crear oyentes de eventos en elementos que existan en el momento en que se configuran los oyentes. Por ejemplo:

```js
$(document).ready(function () {
  // Ahora crea un nuevo elemento de botón con la clase alert.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Configura el comportamiento de clic en todos los elementos de botón con la clase alert
  // que existan en el DOM cuando se ejecuta la instrucción
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

Si se crean elementos similares después de configurar los oyentes de eventos, no recogerán automáticamente los comportamientos de eventos que hayas configurado previamente.

> Puede actualizar la pestaña **Web 8080** para previsualizar la página web.
