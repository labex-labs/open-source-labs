# Como Achatar um Array com JavaScript

Para achatar um array até uma profundidade especificada em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a função `flatten` com dois argumentos: `arr` (o array a ser achatado) e `depth` (o número máximo de níveis aninhados a serem achatados).
3.  Dentro da função `flatten`, use recursão para decrementar `depth` em `1` para cada nível de profundidade.
4.  Use `Array.prototype.reduce()` e `Array.prototype.concat()` para mesclar elementos ou arrays.
5.  Adicione um caso base para quando `depth` for igual a `1` para parar a recursão.
6.  Omita o segundo argumento, `depth`, para achatar apenas até uma profundidade de `1` (achatamento simples).

Aqui está o código para a função `flatten`:

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

Você pode testar a função `flatten` com os seguintes exemplos:

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
