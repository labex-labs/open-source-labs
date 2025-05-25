# Instruções para Mesclar Arrays Ordenados em JavaScript

Para mesclar dois arrays ordenados em JavaScript, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o operador spread (`...`) para clonar ambos os arrays fornecidos.
3.  Use `Array.from()` para criar um array com o comprimento apropriado com base nos arrays fornecidos.
4.  Use `Array.prototype.shift()` para preencher o array recém-criado a partir dos elementos removidos dos arrays clonados.

Aqui está um trecho de código de exemplo para mesclar dois arrays ordenados:

```js
const mergeSortedArrays = (a, b) => {
  const _a = [...a],
    _b = [...b];
  return Array.from({ length: _a.length + _b.length }, () => {
    if (!_a.length) return _b.shift();
    else if (!_b.length) return _a.shift();
    else return _a[0] > _b[0] ? _b.shift() : _a.shift();
  });
};

console.log(mergeSortedArrays([1, 4, 5], [2, 3, 6])); // Output: [1, 2, 3, 4, 5, 6]
```

No código acima, a função `mergeSortedArrays` recebe dois arrays ordenados como argumentos e retorna o array mesclado seguindo as etapas acima. A saída para o código de exemplo é `[1, 2, 3, 4, 5, 6]`.
