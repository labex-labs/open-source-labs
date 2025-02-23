# Cómo ordenar una matriz de objetos según el orden de una propiedad

Para ordenar una matriz de objetos según el orden de una propiedad, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.reduce()` para crear un objeto a partir de la matriz `order` con los valores como claves y su índice original como valor.
3. Utilice `Array.prototype.sort()` para ordenar la matriz dada, saltando los elementos para los cuales `prop` está vacío o no está en la matriz `order`.

A continuación, se muestra un fragmento de código de ejemplo para ordenar una matriz de objetos según el orden de una propiedad:

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

Puede utilizar la función `orderWith` para ordenar una matriz de objetos según el orden de una propiedad. Por ejemplo:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
