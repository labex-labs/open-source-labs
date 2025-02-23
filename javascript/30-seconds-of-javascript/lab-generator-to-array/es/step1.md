# Convertir la salida de un generador en un array

Para convertir la salida de una función generadora en un array, utiliza el operador de propagación (`...`). Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Aquí hay una función de ejemplo que convierte un generador en un array:

```js
const generatorToArray = (gen) => [...gen];
```

Puedes utilizar esta función de la siguiente manera:

```js
const s = new Set([1, 2, 1, 3, 1, 4]);
generatorToArray(s.entries()); // [[ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ]]
```
