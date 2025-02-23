# Convertir valores en arrays en JavaScript

Para convertir un valor en un array, utiliza la función `castArray` proporcionada a continuación.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

Para usar esta función, pasa el valor que quieres convertir como argumento. La función comprobará si el valor ya es un array utilizando `Array.isArray()`. Si es un array, la función devolverá el array tal cual. Si no es un array, la función devolverá el valor encapsulado en un array.

A continuación, se muestra un ejemplo de cómo usar `castArray`:

```js
castArray("foo"); // devuelve: ['foo']
castArray([1]); // devuelve: [1]
```

Para comenzar a practicar la codificación en JavaScript, abre la Terminal o SSH y escribe `node`.
