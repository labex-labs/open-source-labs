# Función para limitar un número dentro de un rango

Para limitar un número dentro de un rango específico, utiliza la función `clampNumber`.

Para comenzar, abre la Terminal/SSH y escribe `node` para practicar la codificación.

La función `clampNumber` toma tres parámetros: `num`, `a` y `b`. Limita `num` dentro del rango inclusivo especificado por los valores límite `a` y `b` y devuelve el resultado.

Si `num` se encuentra dentro del rango, la función devuelve `num`. De lo contrario, devuelve el número más cercano en el rango.

Aquí está el código de la función `clampNumber`:

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

Y aquí hay algunos ejemplos de cómo utilizar la función:

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
