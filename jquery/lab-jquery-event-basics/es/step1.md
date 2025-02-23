# Configuración de respuestas a eventos en elementos DOM

> `index.html` ya se ha proporcionado en la máquina virtual.

jQuery hace que sea sencillo configurar respuestas basadas en eventos en los elementos de la página. Estos eventos a menudo se desencadenan por la interacción del usuario final con la página, como cuando se escribe texto en un elemento de formulario o cuando se mueve el puntero del mouse. En algunos casos, como los eventos de carga y descarga de la página, el navegador mismo desencadenará el evento.

jQuery ofrece métodos de conveniencia para la mayoría de los eventos nativos del navegador. Estos métodos, que incluyen `.click()`, `.focus()`, `.blur()`, `.change()`, etc., son un atajo para el método `.on()` de jQuery. El método on es útil para enlazar la misma función de controlador a múltiples eventos, cuando se desea proporcionar datos a la función de controlador de eventos, cuando se está trabajando con eventos personalizados o cuando se desea pasar un objeto de múltiples eventos y controladores.

```js
// Configuración de evento utilizando un método de conveniencia
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// Configuración de evento equivalente utilizando el método `.on()`
$("p").on("click", function () {
  console.log("click");
});
```

> Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
