# Remover Elementos de um Array da Direita

Para remover um número especificado de elementos da direita de um array, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.slice()` para remover o número especificado de elementos da direita.
3.  Se você quiser remover apenas um elemento, pode omitir o último argumento, `n`, e o valor padrão de `1` será usado.

Aqui está um exemplo de trecho de código:

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

Você pode testar esta função com os seguintes exemplos:

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
