# Cómo reemplazar o agregar un valor en un array

Para reemplazar un elemento en un array o agregarlo si no existe, sigue estos pasos:

1. Utiliza el operador de propagación (`...`) para crear una copia superficial del array.
2. Utiliza `Array.prototype.findIndex()` para encontrar el índice del primer elemento que cumpla con la función de comparación `compFn` proporcionada.
3. Si no se encuentra ningún elemento, utiliza `Array.prototype.push()` para agregar el nuevo valor al array.
4. En caso contrario, utiliza `Array.prototype.splice()` para reemplazar el valor en el índice encontrado con el nuevo valor.

A continuación, se muestra un ejemplo de cómo implementar esta funcionalidad:

```js
const replaceOrAppend = (arr, val, compFn) => {
  const res = [...arr];
  const i = arr.findIndex((v) => compFn(v, val));
  if (i === -1) res.push(val);
  else res.splice(i, 1, val);
  return res;
};
```

Puedes utilizar esta función con un array de objetos de la siguiente manera:

```js
const people = [
  { name: "John", age: 30 },
  { name: "Jane", age: 28 }
];
const jane = { name: "Jane", age: 29 };
const jack = { name: "Jack", age: 28 };
replaceOrAppend(people, jane, (a, b) => a.name === b.name);
// [ { name: 'John', age: 30 }, { name: 'Jane', age: 29 } ]
replaceOrAppend(people, jack, (a, b) => a.name === b.name);
// [
//   { name: 'John', age: 30 },
//   { name: 'Jane', age: 28 },
//   { name: 'Jack', age: 28 }
// ]
```
