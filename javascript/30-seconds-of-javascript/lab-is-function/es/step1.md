# Comprobando si un valor es una función

Para comprobar si un valor es una función, puedes usar el operador `typeof` con el primitivo `function`.

Aquí hay un ejemplo de una función que comprueba si un valor dado es una función:

```js
const isFunction = (val) => typeof val === "function";
```

Puedes usarlo de la siguiente manera:

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
