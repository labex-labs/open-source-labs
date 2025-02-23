# Eventos

> `index.html` ya se ha proporcionado en la máquina virtual.

La interactividad real en un sitio web requiere controladores de eventos. Estos son estructuras de código que escuchan la actividad en el navegador y ejecutan código en respuesta. El ejemplo más obvio es manejar el [evento click](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), que es activado por el navegador cuando haces clic en algo con el mouse. Para demostrar esto, escribe lo siguiente en la consola, luego haz clic en la página web actual:

```js
document.querySelector("html").addEventListener("click", function () {
  alert("¡Ay! ¡Deja de pincharme!");
});
```

Hay varias maneras de adjuntar un controlador de eventos a un elemento.
Aquí seleccionamos el elemento [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html). Luego llamamos a su función [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), pasando el nombre del evento a escuchar (`'click'`) y una función que se ejecutará cuando ocurra el evento.

La función que acabamos de pasar a `addEventListener()` aquí se llama una _función anónima_, porque no tiene un nombre. Hay una forma alternativa de escribir funciones anónimas, que llamamos _función flecha_.
Una función flecha utiliza `() =>` en lugar de `function ()`:

```js
document.querySelector("html").addEventListener("click", () => {
  alert("¡Ay! ¡Deja de pincharme!");
});
```

> Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
