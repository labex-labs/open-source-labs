# Convertir una función variádica

Para convertir una función variádica, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.
2. Crea una función que tome una función variádica.
3. Utiliza una clausura y el operador de propagación (`...`) para mapear la matriz de argumentos a las entradas de la función.
4. Devuelve una nueva función que acepte una matriz de argumentos y llame a la función variádica original con esos argumentos.

Aquí hay un ejemplo de cómo utilizar esta técnica para convertir la función `Math.max`:

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
