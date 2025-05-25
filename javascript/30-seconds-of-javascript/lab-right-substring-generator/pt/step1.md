# Gerador de Substrings à Direita

Para gerar todas as substrings à direita (right substrings) de uma string dada, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `String.prototype.length` para interromper a iteração antecipadamente se a string estiver vazia.
3.  Use um loop `for...in` e `String.prototype.slice()` para `yield` cada substring da string dada, começando pelo final.

Aqui está o trecho de código:

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

Exemplo de uso:

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
