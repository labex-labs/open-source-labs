# Uma Função para Encontrar a Correspondência Numérica Mais Próxima em um Array

Para encontrar o número mais próximo em um array, use a seguinte função:

```js
const closest = (arr, n) =>
  arr.reduce((acc, num) => (Math.abs(num - n) < Math.abs(acc - n) ? num : acc));
```

Veja como usá-la:

1.  Abra o Terminal/SSH.
2.  Digite `node`.
3.  Use a função `closest()` e forneça o array e o valor alvo como argumentos.

Exemplo de uso: `closest([6, 1, 3, 7, 9], 5)` retornará `6`, que é o número mais próximo de `5` no array.
