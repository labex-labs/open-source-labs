# Verificando se Todos os Elementos em um Array são Únicos com uma Função

Para verificar se todos os elementos em um array são únicos com base em uma função de mapeamento fornecida, siga estas etapas:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.map()` para aplicar a função fornecida `fn` a todos os elementos no array `arr`.
3.  Crie um novo `Set` a partir dos valores mapeados para manter apenas ocorrências únicas.
4.  Compare o comprimento dos valores mapeados únicos com o comprimento do array original usando os métodos `Array.prototype.length` e `Set.prototype.size`.

Aqui está o código:

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

Você pode usar a função `allUniqueBy()` para verificar se todos os elementos em um array são únicos. Por exemplo:

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
