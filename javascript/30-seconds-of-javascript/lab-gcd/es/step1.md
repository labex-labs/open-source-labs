# Cómo calcular el máximo común divisor

Para calcular el máximo común divisor entre dos o más números/arrays utilizando código, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. Utilice el siguiente código:

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. La función `gcd` utiliza la recursión.

4. El caso base es cuando `y` es igual a `0`. En este caso, la función devuelve `x`.

5. De lo contrario, la función devuelve el MCD de `y` y el resto de la división `x / y`.

6. Para probar la función, use el siguiente código:

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
