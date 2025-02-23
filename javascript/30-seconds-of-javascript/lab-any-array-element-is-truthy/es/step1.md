# Probando si algún elemento de un array es verdadero

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para comprobar si algún elemento de una colección devuelve `true` en base a una función proporcionada, utiliza `Array.prototype.some()`. Si quieres utilizar la función `Boolean` como predeterminada, puedes omitir el segundo argumento, `fn`.

A continuación, se muestra un ejemplo de código:

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

Puedes probarlo con los siguientes ejemplos:

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
