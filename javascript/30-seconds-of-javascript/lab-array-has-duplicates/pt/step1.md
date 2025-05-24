# Como Verificar por Duplicatas em um Array

Para verificar se um array possui valores duplicados, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Set` para obter os valores únicos no array.
3.  Use `Set.prototype.size` e `Array.prototype.length` para verificar se a contagem dos valores únicos é a mesma que o número de elementos no array original.

Aqui está um trecho de código de exemplo que verifica por duplicatas em um array:

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

Você pode testar esta função com o seguinte código:

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

A função `hasDuplicates` retorna `true` se houver quaisquer valores duplicados no array e `false` caso contrário.
