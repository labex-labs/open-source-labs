# Removendo Chaves de Objetos com Base em uma Função Callback

Para remover chaves de objetos com base em uma função _callback_, use a função `omitBy`.

- `omitBy` cria um objeto consistindo em propriedades que retornam _falsy_ para a função fornecida.
- `Object.keys()` e `Array.prototype.filter()` são usados para remover chaves para as quais `fn` retorna um valor _truthy_.
- `Array.prototype.reduce()` converte as chaves filtradas de volta para um objeto com os pares chave-valor correspondentes.
- A função _callback_ recebe dois argumentos: `value` e `key`.
- O exemplo abaixo mostra como `omitBy` é usado para remover chaves numéricas de um objeto.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
