# Cómo comprobar si un valor es nulo o indefinido en JavaScript

Para determinar si un valor es `null` o `undefined` en JavaScript, puedes utilizar el operador de igualdad estricta (`===`). Aquí hay un fragmento de código de ejemplo que comprueba si el valor especificado es `null` o `undefined`:

```js
const isNil = (val) => val === undefined || val === null;
```

Puedes utilizar esta función para comprobar si un valor es `null` o `undefined`, de la siguiente manera:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

Para comenzar a practicar la programación en JavaScript, puedes abrir la Terminal/SSH y escribir `node`.
