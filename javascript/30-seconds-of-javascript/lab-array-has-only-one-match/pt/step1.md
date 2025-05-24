# Função para Verificar se o Array Possui Apenas Uma Correspondência

Para verificar se um array possui apenas um valor correspondente à função fornecida, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.filter()` em combinação com `fn` para encontrar todos os elementos do array correspondentes.
3.  Use `Array.prototype.length` para verificar se apenas um elemento corresponde a `fn`.

Aqui está o código:

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

E aqui está um exemplo:

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
