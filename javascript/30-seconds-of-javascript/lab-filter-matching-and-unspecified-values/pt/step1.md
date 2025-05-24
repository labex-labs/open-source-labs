# Filtrando Objetos por Condição e Chaves

Para filtrar um array de objetos com base em uma condição, ao mesmo tempo em que filtra chaves não especificadas, use a função `reducedFilter()`.

Aqui estão os passos a seguir:

1.  Use `Array.prototype.filter()` para filtrar o array com base no predicado `fn`, de modo que retorne os objetos para os quais a condição retornou um valor verdadeiro (truthy).

2.  Use `Array.prototype.map()` no array filtrado para retornar o novo objeto.

3.  Use `Array.prototype.reduce()` para filtrar as chaves que não foram fornecidas como argumento `keys`.

```js
const reducedFilter = (data, keys, fn) =>
  data.filter(fn).map((el) =>
    keys.reduce((acc, key) => {
      acc[key] = el[key];
      return acc;
    }, {})
  );
```

Aqui está um exemplo de uso da função `reducedFilter()`:

```js
const data = [
  {
    id: 1,
    name: "john",
    age: 24
  },
  {
    id: 2,
    name: "mike",
    age: 50
  }
];

reducedFilter(data, ["id", "name"], (item) => item.age > 24);
// Output: [{ id: 2, name: 'mike'}]
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
