# Complemento Lógico

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para obtener el complemento lógico de una función `fn`, utiliza la función `complement`. Esta función devuelve otra función que aplica el operador lógico no (`!`) sobre el resultado de llamar a `fn` con cualquier argumento suministrado.

Aquí hay un fragmento de código de ejemplo:

```js
const complement =
  (fn) =>
  (...args) =>
    !fn(...args);
```

Para usar esta función, define una función predicado, por ejemplo, `isEven` que devuelve `true` si un número dado es par. Luego, puedes obtener el complemento lógico de esta función utilizando la función `complement`, como se muestra a continuación:

```js
const isEven = (num) => num % 2 === 0;
const isOdd = complement(isEven);
isOdd(2); // false
isOdd(3); // true
```
