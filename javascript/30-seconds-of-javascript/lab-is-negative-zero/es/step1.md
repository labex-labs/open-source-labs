# Verificación de cero negativo

Para verificar si un número es cero negativo, abre la Terminal/SSH y escribe `node`. Luego, utiliza el siguiente código:

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

Esto verificará si el valor pasado es igual a `0` y si `1` dividido por el valor es igual a `-Infinity`. Por ejemplo:

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
