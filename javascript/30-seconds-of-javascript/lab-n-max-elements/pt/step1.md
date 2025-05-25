# Como Obter N Elementos Máximos de um Array em JavaScript

Para praticar a codificação em JavaScript, abra o Terminal/SSH e digite `node`. Depois de fazer isso, você pode usar as seguintes etapas para obter os `n` elementos máximos de um array:

1.  Use `Array.prototype.sort()` junto com o operador spread (`...`) para criar um clone raso (shallow clone) do array e ordená-lo em ordem decrescente.
2.  Use `Array.prototype.slice()` para obter o número especificado de elementos.
3.  Se você omitir o segundo argumento, `n`, você obterá um array de um elemento por padrão.
4.  Se `n` for maior ou igual ao comprimento do array fornecido, então retorne o array original (ordenado em ordem decrescente).

Aqui está o código JavaScript para a função `maxN` que implementa essas etapas:

```js
const maxN = (arr, n = 1) => [...arr].sort((a, b) => b - a).slice(0, n);
```

Você pode testar a função `maxN` com os seguintes exemplos:

```js
maxN([1, 2, 3]); // [3]
maxN([1, 2, 3], 2); // [3, 2]
```
