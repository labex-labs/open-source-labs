# Usando la coalescencia de argumentos

Para comenzar a codificar, abre la Terminal/SSH y escribe `node`. La coalescencia de argumentos es una técnica utilizada para devolver el primer argumento definido y no nulo en una lista de argumentos. Para lograr esto, utiliza `Array.prototype.find()` y `Array.prototype.includes()` para encontrar el primer valor que no sea igual a `undefined` o `null`.

Aquí hay un ejemplo de cómo utilizar la coalescencia de argumentos en JavaScript:

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

En el fragmento de código anterior, `coalesce` es una función que toma cualquier número de argumentos y devuelve el primer argumento definido y no nulo. Aquí hay un ejemplo de cómo utilizar la función `coalesce`:

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

En este ejemplo, `coalesce` se llama con una lista de argumentos que incluye `null`, `undefined`, una cadena vacía `''`, `NaN` y la cadena `'Waldo'`. La función devuelve una cadena vacía `''` porque es el primer argumento definido y no nulo en la lista.
