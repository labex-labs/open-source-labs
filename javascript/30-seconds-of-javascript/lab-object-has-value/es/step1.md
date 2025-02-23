# Función para comprobar si un objeto contiene un valor específico

Para comprobar si un objeto contiene un valor específico, utiliza la siguiente función:

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

Para utilizar esta función, pasa el objeto que quieres buscar y el valor objetivo como argumentos. La función devolverá `true` si el objeto contiene el valor y `false` si no lo contiene.

Aquí hay un ejemplo:

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.
