# Verificando se um Array Inclui Quaisquer Valores

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Para verificar se um array inclui pelo menos um elemento de outro array, use `Array.prototype.some()` e `Array.prototype.includes()`. Aqui está um exemplo de função:

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

Você pode chamar esta função e passar os dois arrays que deseja comparar como argumentos. A função retornará um valor booleano indicando se pelo menos um elemento de `values` está incluído em `arr`. Aqui estão alguns exemplos:

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
