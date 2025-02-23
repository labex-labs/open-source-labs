# Función para Combinar Arrays de Objetos Basados en una Clave Específica

Para combinar dos arrays de objetos basados en una clave específica, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Array.prototype.reduce()` con un acumulador de objeto para combinar todos los objetos en ambos arrays basados en la `prop` dada.
3. Utiliza `Object.values()` para convertir el objeto resultante en un array y devolverlo.

Aquí está la función que puedes utilizar:

```js
const combine = (a, b, prop) =>
  Object.values(
    [...a, ...b].reduce((acc, v) => {
      if (v[prop])
        acc[v[prop]] = acc[v[prop]] ? { ...acc[v[prop]], ...v } : { ...v };
      return acc;
    }, {})
  );
```

Aquí hay un ejemplo de cómo utilizar esta función:

```js
const x = [
  { id: 1, name: "John" },
  { id: 2, name: "Maria" }
];
const y = [{ id: 1, age: 28 }, { id: 3, age: 26 }, { age: 3 }];
combine(x, y, "id");
// [
//  { id: 1, name: 'John', age: 28 },
//  { id: 2, name: 'Maria' },
//  { id: 3, age: 26 }
// ]
```
