# Cómo filtrar valores únicos en una matriz usando JavaScript

Para filtrar valores únicos en una matriz usando JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el constructor `Set` y el operador de propagación (`...`) para crear una matriz con los valores únicos de tu matriz original.
3. Utiliza `Array.prototype.filter()` para crear una matriz que contenga solo los valores no únicos.
4. Define una función llamada `filterUnique` que tome una matriz como argumento y le aplique los pasos anteriores.
5. Llama a la función `filterUnique` con tu matriz como argumento.

A continuación, se muestra un fragmento de código de ejemplo para lograr esto:

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

En el fragmento de código anterior, la función `filterUnique` toma una matriz y le aplica el constructor `Set` y el método `Array.prototype.filter()` para devolver una matriz con solo los valores no únicos.
