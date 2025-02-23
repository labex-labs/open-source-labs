# Mostrando y Ocultando Contenido

> `index.html` ya se ha proporcionado en la VM.

jQuery puede mostrar u ocultar contenido instantáneamente con `.show()` o `.hide()`:

```js
// Ocultar instantáneamente todos los párrafos
$("p").hide();

// Mostrar instantáneamente todos los divs que tienen la clase de estilo oculta
$("div.hidden").show();
```

Cuando jQuery oculta un elemento, establece su propiedad CSS `display` en `none`. Esto significa que el contenido tendrá un ancho y altura de cero; no significa que el contenido simplemente se tornará transparente y dejará un área vacía en la página.

jQuery también puede mostrar u ocultar contenido mediante efectos de animación. Puedes decir a `.show()` y `.hide()` que usen animación de varias maneras. Una es pasar un argumento de `'slow'`, `'normal'` o `'fast'`:

```js
// Ocultar lentamente todos los párrafos
$("p").hide("slow");

// Mostrar rápidamente todos los divs que tienen la clase de estilo oculta
$("div.hidden").show("fast");
```

Si prefieres un control más directo sobre la duración del efecto de animación, puedes pasar la duración deseada en milisegundos a `.show()` y `.hide()`:

```js
// Ocultar todos los párrafos en medio segundo
$("p").hide(2000);

// Mostrar todos los divs que tienen la clase de estilo oculta en 1,25 segundos
$("div.hidden").show(1250);
```

La mayoría de los desarrolladores pasan un número de milisegundos para tener un control más preciso sobre la duración.

> Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
