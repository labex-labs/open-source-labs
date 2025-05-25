# Convertendo um Valor para um Inteiro Seguro

Para converter um valor em um inteiro seguro, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Math.max()` e `Math.min()` para encontrar o valor seguro mais próximo.
3. Use `Math.round()` para converter o valor em um inteiro.

Aqui está um trecho de código de exemplo que demonstra como converter um valor em um inteiro seguro:

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

Você pode testar esta função com a seguinte entrada:

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
