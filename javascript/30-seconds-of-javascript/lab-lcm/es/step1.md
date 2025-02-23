# Calculando el mínimo común múltiplo

Para calcular el mínimo común múltiplo de dos o más números, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la fórmula del máximo común divisor (MCD) y el hecho de que `mcm(x, y) = x * y / mcd(x, y)` para determinar el mínimo común múltiplo.
3. La fórmula del MCD utiliza la recursión.
4. Implemente el siguiente código en JavaScript:

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

Uso de ejemplo:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
