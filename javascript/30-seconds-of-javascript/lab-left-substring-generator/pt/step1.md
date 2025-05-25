# Prática de Código: Gerador de Substrings à Esquerda

Para gerar todas as substrings à esquerda de uma string dada, use a função `leftSubstrGenerator` fornecida abaixo.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

Para usar a função, abra o Terminal/SSH e digite `node`. Em seguida, insira a função com um argumento de string:

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

A função usa `String.prototype.length` para terminar antecipadamente se a string estiver vazia e um loop `for...in` com `String.prototype.slice()` para `yield` cada substring da string dada, começando no início.
