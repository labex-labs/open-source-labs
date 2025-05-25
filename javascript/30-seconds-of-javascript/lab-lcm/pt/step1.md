# Calculando o Mínimo Múltiplo Comum

Para calcular o mínimo múltiplo comum de dois ou mais números, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a fórmula do máximo divisor comum (MDC) e o fato de que `mmc(x, y) = x * y / mdc(x, y)` para determinar o mínimo múltiplo comum.
3.  A fórmula do MDC utiliza recursão.
4.  Implemente o seguinte código em JavaScript:

```js
const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y));
  const _lcm = (x, y) => (x * y) / gcd(x, y);
  return [...arr].reduce((a, b) => _lcm(a, b));
};
```

Exemplo de uso:

```js
lcm(12, 7); // 84
lcm(...[1, 3, 4, 5]); // 60
```
