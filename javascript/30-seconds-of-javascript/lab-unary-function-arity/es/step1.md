# Comprendiendo la aridad de las funciones unarias

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`.

La aridad de una función unaria se refiere a una función que toma solo un argumento, ignorando cualquier argumento adicional.

La función `fn` proporcionada se puede llamar solo con el primer argumento suministrado. Para crear una función unaria, utiliza el siguiente código:

```js
const unary = (fn) => (val) => fn(val);
```

Un ejemplo de uso de `unary` con la función `parseInt` se muestra a continuación:

```js
["6", "8", "10"].map(unary(parseInt)); // [6, 8, 10]
```
