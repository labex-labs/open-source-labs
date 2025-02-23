# Comprobar si un número es una potencia de diez

Para comprobar si un número es una potencia de diez, abre la Terminal/SSH y escribe `node`.

Aquí está el código que puedes utilizar para determinar si `n` es una potencia de `10`:

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Utiliza la función `isPowerOfTen()` para determinar si un número dado es una potencia de diez.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
