# Função para selecionar chaves de objeto que correspondem a uma condição dada

Para selecionar chaves de objeto que correspondem a uma condição dada, use a função `pickBy()`. Esta função cria um novo objeto composto pelas propriedades para as quais a função fornecida retorna um valor verdadeiro (truthy).

- Use `Object.keys()` e `Array.prototype.filter()` para remover as chaves para as quais `fn` retorna um valor falso (falsy).
- Use `Array.prototype.reduce()` para converter as chaves filtradas de volta em um objeto com os pares chave-valor correspondentes.
- A função de callback é invocada com dois argumentos: (valor, chave).

Aqui está o código para a função `pickBy()`:

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

Você pode usar esta função para selecionar chaves que correspondem a uma condição. Por exemplo:

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
