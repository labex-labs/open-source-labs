# Uma função que obtém o n-ésimo argumento

Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`. Veja como você pode criar uma função que obtém o argumento no índice `n`.

- Use `Array.prototype.slice()` para obter o argumento desejado no índice `n`.
- Se `n` for negativo, o n-ésimo argumento do final é retornado.

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

Aqui está um exemplo de como usar a função `nthArg`:

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // Output: 3
console.log(third(1, 2)); // Output: undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // Output: 5
```
