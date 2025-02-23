# Cómo reordenar los argumentos de una función en JavaScript

Para reordenar los argumentos de una función en JavaScript, puedes utilizar la función `rearg()`. Primero, crea una función que invoque la función proporcionada con sus argumentos organizados de acuerdo con los índices especificados. Puedes utilizar `Array.prototype.map()` para reordenar los argumentos basados en `indexes`. Luego, utiliza el operador de propagación (`...`) para pasar los argumentos transformados a `fn`.

Aquí hay un ejemplo de cómo utilizar la función `rearg()`:

```js
const rearg =
  (fn, indexes) =>
  (...args) =>
    fn(...indexes.map((i) => args[i]));
```

En este ejemplo, utilizamos `rearg()` para crear una nueva función que reordena los argumentos de otra función.

```js
var rearged = rearg(
  function (a, b, c) {
    return [a, b, c];
  },
  [2, 0, 1]
);
rearged("b", "c", "a"); // ['a', 'b', 'c']
```

En el código anterior, creamos una nueva función `rearged` que reordena los argumentos de la función `function(a, b, c) { return [a, b, c]; }`. El argumento `indexes` especifica el orden en el que se deben reordenar los argumentos. En este caso, queremos que el tercer argumento venga primero, el primer argumento venga segundo y el segundo argumento venga tercero. Cuando llamamos a `rearged('b', 'c', 'a')`, devuelve `['a', 'b', 'c']`, que es el resultado de llamar a la función original con los argumentos reordenados.
