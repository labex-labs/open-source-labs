# Cómo mapear una matriz a un objeto en JavaScript

Para mapear una matriz de objetos a un objeto en JavaScript, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.reduce()` para mapear la matriz a un objeto.
3. Utiliza el parámetro `mapKey` para mapear las claves del objeto y el parámetro `mapValue` para mapear los valores.

A continuación, se muestra un fragmento de código de ejemplo que demuestra cómo utilizar la función `objectify` para mapear una matriz de objetos a un objeto:

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

Luego, puedes utilizar la función `objectify` para mapear una matriz de objetos a un objeto de las siguientes maneras:

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// Mapea la matriz de objetos a un objeto utilizando la propiedad name como claves
objectify(people, (p) => p.name.toLowerCase());
// Salida: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// Mapea la matriz de objetos a un objeto utilizando la propiedad name como claves y la propiedad age como valores
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Salida: { john: 42, adam: 39 }
```
