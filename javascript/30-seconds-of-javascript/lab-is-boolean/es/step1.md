# Comprobando si un valor es booleano

Para comprobar si un valor es un primitivo booleano en JavaScript, utiliza el operador `typeof` con el operador de comparación `===`.

```js
const isBoolean = (val) => typeof val === "boolean";
```

A continuación, se muestra un ejemplo de cómo utilizar la función `isBoolean()` para comprobar si un valor es booleano:

```js
isBoolean(null); // devuelve false
isBoolean(false); // devuelve true
```

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
