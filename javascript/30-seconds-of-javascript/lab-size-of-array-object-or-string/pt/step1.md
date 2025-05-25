# Função para Obter o Tamanho de Array, Objeto ou String

Para usar esta função, abra o Terminal/SSH e digite `node`. Esta função obtém o tamanho de um array, objeto ou string.

Para usá-la:

- Determine o tipo de `val` (`array`, `object` ou `string`).
- Use a propriedade `Array.prototype.length` para arrays.
- Use o valor `length` ou `size` se disponível, ou o número de chaves para objetos.
- Para strings, use o `size` de um objeto [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) criado a partir de `val`.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

Exemplos:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
