# Instruções para Selecionar Chaves de Objeto

Para selecionar pares chave-valor específicos de um objeto, use a função `pick(obj, arr)`.

- Passe o objeto como o primeiro argumento e um array de chaves para selecionar como o segundo argumento.
- A função retorna um novo objeto com apenas os pares chave-valor que correspondem às chaves fornecidas.

Aqui está um exemplo de como usar `pick()`:

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.
