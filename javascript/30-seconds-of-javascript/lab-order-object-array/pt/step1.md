# Como Ordenar um Array de Objetos em JavaScript

Para ordenar um array de objetos em JavaScript, você pode usar o método `Array.prototype.sort()` e o método `Array.prototype.reduce()` no array `props` com um valor padrão de `0`.

Aqui está um exemplo de função, `orderBy`, que ordena um array de objetos com base nas propriedades e ordens especificadas:

```js
const orderBy = (arr, props, orders = ["asc"]) =>
  [...arr].sort((a, b) =>
    props.reduce((acc, prop, i) => {
      if (acc === 0) {
        const [p1, p2] =
          orders[i] === "desc" ? [b[prop], a[prop]] : [a[prop], b[prop]];
        acc = p1 > p2 ? 1 : p1 < p2 ? -1 : 0;
      }
      return acc;
    }, 0)
  );
```

Para usar esta função, passe um array de objetos, um array de propriedades para ordenar e um array opcional de ordens. Se nenhum array `orders` for fornecido, a função irá ordenar por `'asc'` por padrão.

Aqui estão alguns exemplos de como usar a função `orderBy`:

```js
const users = [
  { name: "fred", age: 48 },
  { name: "barney", age: 36 },
  { name: "fred", age: 40 }
];

// ordenar por nome ascendente e idade descendente
orderBy(users, ["name", "age"], ["asc", "desc"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 48}, {name: 'fred', age: 40}]

// ordenar por nome ascendente e idade ascendente (ordem padrão)
orderBy(users, ["name", "age"]);
// Output: [{name: 'barney', age: 36}, {name: 'fred', age: 40}, {name: 'fred', age: 48}]
```
