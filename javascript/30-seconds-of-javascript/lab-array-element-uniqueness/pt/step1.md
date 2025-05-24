# Como Verificar se Todos os Elementos de um Array São Únicos

Para verificar se todos os elementos em um array são únicos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie um novo `Set` a partir dos valores mapeados para manter apenas ocorrências únicas.
3.  Use `Array.prototype.length` e `Set.prototype.size` para comparar o comprimento dos valores únicos com o array original.

Aqui está um exemplo de função que implementa esses passos:

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

Você pode usar esta função para verificar se um array tem todos os elementos únicos assim:

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
