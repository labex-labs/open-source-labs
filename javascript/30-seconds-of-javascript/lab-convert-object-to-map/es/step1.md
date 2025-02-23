# Así se convierte un objeto en un Map

Para convertir un objeto en un `Map`, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Object.entries()` para convertir el objeto en una matriz de pares clave-valor.
3. Utiliza el constructor `Map` para convertir la matriz en un `Map`.

Aquí hay un fragmento de código de ejemplo:

```js
const objectToMap = (obj) => new Map(Object.entries(obj));
```

Puedes utilizar la función `objectToMap()` para convertir un objeto en un `Map`. Por ejemplo:

```js
objectToMap({ a: 1, b: 2 }); // Map {'a' => 1, 'b' => 2}
```
