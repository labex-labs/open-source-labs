# Função para Verificar se um Array Possui Múltiplas Correspondências

Para verificar se um array possui mais de um valor correspondente a uma função fornecida, siga estas etapas:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.filter()` em combinação com `fn` para encontrar todos os elementos do array correspondentes.
3. Use `Array.prototype.length` para verificar se mais de um elemento corresponde a `fn`.

Aqui está o código que você pode usar:

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

E aqui estão alguns exemplos:

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
