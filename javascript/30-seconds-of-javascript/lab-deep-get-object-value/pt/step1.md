# Como Recuperar um Valor Aninhado em um Objeto Usando um Array de Chaves

Para recuperar um valor específico de um objeto JSON aninhado, você pode usar a função `deepGet`. Esta função recebe um objeto e um array de chaves e retorna o valor alvo se ele existir no objeto.

Para usar a função `deepGet`:

- Crie um array das chaves que você deseja recuperar do objeto JSON aninhado.
- Chame a função `deepGet` com o objeto e o array de chaves.
- A função retornará o valor alvo se ele existir, ou `null` se não existir.

Aqui está o código para a função `deepGet`:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

E aqui está um exemplo de como usar a função `deepGet`:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // returns 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // returns null
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
