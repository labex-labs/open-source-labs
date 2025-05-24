# Como Encontrar a Similaridade de Array em JavaScript

Para praticar a codificação, abra o Terminal/SSH e digite `node`. Isso ajudará você a entender como encontrar um array de elementos que aparecem em ambos os arrays. Siga estes passos:

1.  Use o método `Array.prototype.includes()` para determinar os valores que não fazem parte de `values`.
2.  Use o método `Array.prototype.filter()` para removê-los.

Aqui está o código para encontrar a similaridade de array:

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

Você pode testar este código executando o seguinte comando:

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

Isso retornará `[1, 2]` como saída.
