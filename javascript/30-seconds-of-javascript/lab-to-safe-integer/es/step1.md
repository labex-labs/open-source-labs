# Convertir un valor en un entero seguro

Para convertir un valor en un entero seguro, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza `Math.max()` y `Math.min()` para encontrar el valor seguro más cercano.
3. Utiliza `Math.round()` para convertir el valor en un entero.

A continuación, se muestra un fragmento de código de ejemplo que demuestra cómo convertir un valor en un entero seguro:

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

Puedes probar esta función con la siguiente entrada:

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
