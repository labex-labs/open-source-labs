# Comprobando si todos los elementos de un array son `true`

Para comprobar si todos los elementos de una colección son `true`, puedes usar el método `Array.prototype.every()`. Este método toma una función predicado como argumento y devuelve `true` si la función evalúa a `true` para todos los elementos del array.

Para simplificar el código, puedes usar una función llamada `all` que toma un array y una función predicado opcional como argumentos. La función utiliza `Array.prototype.every()` para comprobar si todos los elementos del array devuelven `true` en base a la función proporcionada. Si no se proporciona ninguna función, se usa `Boolean` como predeterminado.

Aquí hay un ejemplo de cómo usar la función `all`:

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
