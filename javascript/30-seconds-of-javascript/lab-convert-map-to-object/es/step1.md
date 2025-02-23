# Instrucciones para convertir un Map en un objeto en JavaScript

Para convertir un `Map` de JavaScript en un objeto, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Map.prototype.entries()` para convertir el `Map` en una matriz de pares clave-valor.
3. Utilice el método `Object.fromEntries()` para convertir la matriz en un objeto.

A continuación, se muestra un fragmento de código de ejemplo para convertir un `Map` en un objeto:

```js
const mapToObject = (map) => Object.fromEntries(map.entries());
```

Para probar la función, puede ejecutar:

```js
mapToObject(
  new Map([
    ["a", 1],
    ["b", 2]
  ])
); // {a: 1, b: 2}
```
