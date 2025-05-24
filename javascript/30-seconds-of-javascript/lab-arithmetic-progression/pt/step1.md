# Exemplo de Código de Progressão Aritmética

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está um exemplo de código que cria um array de números em progressão aritmética. O array começa com um inteiro positivo dado e vai até um limite especificado:

```js
const arithmeticProgression = (n, lim) =>
  Array.from({ length: Math.ceil(lim / n) }, (_, i) => (i + 1) * n);
```

Para usar este código, basta chamar a função `arithmeticProgression` com dois argumentos: o inteiro positivo inicial e o limite. Por exemplo:

```js
arithmeticProgression(5, 25); // [5, 10, 15, 20, 25]
```
