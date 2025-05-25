# Verificar se um Número é uma Potência de Dois

Para verificar se um número é uma potência de dois, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador AND binário bit a bit (`&`) para determinar se o número (`n`) é uma potência de `2`.
3.  Adicionalmente, verifique se `n` não é falsy.
4.  O seguinte código verifica funcionalmente se `n` é uma potência de dois:

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

Aqui estão alguns exemplos de como usar a função `isPowerOfTwo`:

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
