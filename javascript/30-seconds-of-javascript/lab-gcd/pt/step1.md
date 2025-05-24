# Como Calcular o Maior Divisor Comum

Para calcular o maior divisor comum (MDC - Greatest Common Divisor) entre dois ou mais números/arrays usando código, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use o seguinte código:

```js
const gcd = (...arr) => {
  const _gcd = (x, y) => (!y ? x : gcd(y, x % y));
  return [...arr].reduce((a, b) => _gcd(a, b));
};
```

3. A função `gcd` usa recursão.

4. O caso base é quando `y` é igual a `0`. Neste caso, a função retorna `x`.

5. Caso contrário, a função retorna o MDC de `y` e o resto da divisão `x / y`.

6. Para testar a função, use o seguinte código:

```js
gcd(8, 36); // 4
gcd(...[12, 8, 32]); // 4
```
