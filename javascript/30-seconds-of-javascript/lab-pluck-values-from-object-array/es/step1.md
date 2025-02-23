# Instrucciones para extraer valores de una matriz de objetos

Para extraer valores de una matriz de objetos, puedes seguir estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.map()` para mapear la matriz de objetos al valor de una `clave` especificada para cada objeto.
3. Implemente la siguiente función:

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. Pruebe la función con una matriz de objetos de ejemplo:

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

Esto devolverá una matriz de valores correspondientes a la `clave` especificada de la matriz de objetos.
