# Verificando la igualdad aproximada de números en JavaScript

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Este código verifica si dos números son aproximadamente iguales entre sí. Para hacer esto:

- Utiliza el método `Math.abs()` para comparar la diferencia absoluta de los dos valores con `epsilon`.
- Si no proporcionas un tercer argumento, `epsilon`, la función utilizará un valor predeterminado de `0.001`.

Aquí está el código:

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

Para probar la función, puedes llamarla con dos números como argumentos, así:

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

Esto devolverá `true` porque `Math.PI / 2.0` es aproximadamente igual a `1.5708` con un épsilon de `0.001`.
