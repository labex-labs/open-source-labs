# Función para comprobar si un número está dentro de un rango dado

Para comprobar si un número se encuentra dentro de un rango especificado, utiliza la función `inRange`. Comienza abriendo la Terminal/SSH y escribiendo `node` para comenzar a codificar.

A continuación, se presentan los pasos para utilizar la función `inRange`:

1. Utiliza comparaciones aritméticas para comprobar si el número dado está en el rango especificado.
2. Si el segundo argumento, `end`, no está especificado, el rango se considera que va de `0` a `start`.
3. La función `inRange` toma tres argumentos: `n`, `start` y `end`.
4. Si `end` es menor que `start`, la función intercambia los valores de `start` y `end`.
5. Si `end` no está especificado, la función comprueba si `n` es mayor o igual que 0 y menor que `start`.
6. Si `end` está especificado, la función comprueba si `n` es mayor o igual que `start` y menor que `end`.
7. La función devuelve `true` si `n` está dentro del rango especificado, y `false` en caso contrario.

A continuación, se presenta la función `inRange`:

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

A continuación, se presentan algunos ejemplos de cómo utilizar la función `inRange`:

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
