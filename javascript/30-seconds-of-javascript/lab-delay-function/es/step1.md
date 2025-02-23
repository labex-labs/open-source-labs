# Cómo retrasar la ejecución de una función en JavaScript

Para retrasar la ejecución de una función en JavaScript, puedes usar el método `setTimeout()`. Aquí está cómo hacerlo:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza la siguiente sintaxis para retrasar la ejecución de una función `fn` por `ms` milisegundos:

```js
const delay = (fn, ms, ...args) => setTimeout(fn, ms, ...args);
```

3. Para pasar argumentos a la función, utiliza el operador de propagación (`...`) de esta manera:

```js
delay(
  function (text) {
    console.log(text);
  },
  1000,
  "más tarde"
); // Muestra'más tarde' después de un segundo.
```

Con este código, la función `fn` proporcionada se invocará después del número especificado de milisegundos (`ms`). El parámetro `...args` te permite pasar un número arbitrario de argumentos a la función.
