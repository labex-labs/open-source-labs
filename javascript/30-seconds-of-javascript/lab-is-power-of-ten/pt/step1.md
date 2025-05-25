# Verificar se um Número é uma Potência de Dez

Para verificar se um número é uma potência de dez, abra o Terminal/SSH e digite `node`.

Aqui está o código que você pode usar para determinar se `n` é uma potência de `10`:

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

Use a função `isPowerOfTen()` para determinar se um determinado número é uma potência de dez.

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
