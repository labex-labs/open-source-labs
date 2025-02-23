# Cómo encontrar la fecha mínima en JavaScript

Para encontrar el valor mínimo de fecha en JavaScript, puedes usar la sintaxis de propagación ES6 con `Math.min()` y el constructor `Date`. Aquí hay un fragmento de código de ejemplo:

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

Para usar esta función, crea una matriz de objetos `Date` y pásala a `minDate()` usando la sintaxis de propagación. Aquí hay un ejemplo:

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Devuelve un objeto `Date` que representa 2016-01-08T22:00:00.000Z
```

Al usar este código, puedes encontrar fácilmente el valor mínimo de fecha en JavaScript.
