# Cómo ordenar alfabéticamente una matriz basada en una propiedad dada en JavaScript

Para ordenar alfabéticamente una matriz de objetos basada en una propiedad dada en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `Array.prototype.sort()` para ordenar la matriz basada en la propiedad dada.
3. Utilice `String.prototype.localeCompare()` para comparar los valores de la propiedad dada.

A continuación, se muestra un fragmento de código de ejemplo que puede utilizar:

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

Puede llamar a la función `alphabetical` con una matriz de objetos y la función getter que devuelve la propiedad por la que se debe ordenar. A continuación, se muestra un ejemplo de uso:

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
