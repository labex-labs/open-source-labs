# Cómo recuperar un valor anidado en un objeto utilizando una matriz de claves

Para recuperar un valor específico de un objeto JSON anidado, puedes utilizar la función `deepGet`. Esta función recibe un objeto y una matriz de claves, y devuelve el valor objetivo si existe en el objeto.

Para utilizar la función `deepGet`:

- Crea una matriz de las claves que quieres recuperar del objeto JSON anidado.
- Llama a la función `deepGet` con el objeto y la matriz de claves.
- La función devolverá el valor objetivo si existe, o `null` si no existe.

Aquí está el código de la función `deepGet`:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

Y aquí está un ejemplo de cómo utilizar la función `deepGet`:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // devuelve 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // devuelve null
```

Para comenzar a practicar la programación, abre la Terminal/SSH y escribe `node`.
