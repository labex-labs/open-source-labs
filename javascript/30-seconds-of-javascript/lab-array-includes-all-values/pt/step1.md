# Função para Verificar se um Array Inclui Todos os Valores

Se você deseja verificar se todos os elementos em um array `values` estão incluídos em outro array `arr`, você pode usar a função `includesAll` em JavaScript.

Para começar a usar a função, abra o Terminal/SSH e digite `node`.

Veja como a função `includesAll` funciona:

- Ela usa os métodos `Array.prototype.every()` e `Array.prototype.includes()` para verificar se todos os elementos em `values` estão incluídos em `arr`.
- Se todos os elementos em `values` estiverem incluídos em `arr`, a função retornará `true`. Caso contrário, retornará `false`.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Aqui está um exemplo de como usar a função `includesAll`:

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
