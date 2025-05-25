# Como Ordenar um Array Alfabeticamente com Base em uma Propriedade Específica em JavaScript

Para ordenar um array de objetos alfabeticamente com base em uma propriedade específica em JavaScript, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Array.prototype.sort()` para ordenar o array com base na propriedade fornecida.
3.  Use `String.prototype.localeCompare()` para comparar os valores da propriedade fornecida.

Aqui está um trecho de código de exemplo que você pode usar:

```js
const alphabetical = (arr, getter, order = "asc") =>
  arr.sort(
    order === "desc"
      ? (a, b) => getter(b).localeCompare(getter(a))
      : (a, b) => getter(a).localeCompare(getter(b))
  );
```

Você pode chamar a função `alphabetical` com um array de objetos e a função getter que retorna a propriedade a ser ordenada. Aqui está um exemplo de uso:

```js
const people = [{ name: "John" }, { name: "Adam" }, { name: "Mary" }];
alphabetical(people, (g) => g.name);
// [ { name: 'Adam' }, { name: 'John' }, { name: 'Mary' } ]
alphabetical(people, (g) => g.name, "desc");
// [ { name: 'Mary' }, { name: 'John' }, { name: 'Adam' } ]
```
