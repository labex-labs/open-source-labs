# Como Dividir um Array em Chunks de um Tamanho Específico

Para praticar a codificação, abra o Terminal/SSH e digite `node`.

Para dividir um array em arrays menores de um tamanho especificado, siga estes passos:

1.  Use `Array.from()` para criar um novo array que se ajuste ao número de chunks que serão produzidos.
2.  Use `Array.prototype.slice()` para mapear cada elemento do novo array para um chunk do tamanho de `size`.
3.  Se o array original não puder ser dividido uniformemente, o chunk final conterá os elementos restantes.

Aqui está um exemplo de trecho de código:

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

Você pode usar esta função passando o array que deseja dividir e o tamanho desejado dos chunks. Por exemplo:

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
