# Verificando se um Valor é uma Função Geradora

Para verificar se um valor é uma função geradora, você pode usar a função `isGeneratorFunction`. Para começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

Aqui está como a função `isGeneratorFunction` funciona:

- Ela verifica se o argumento fornecido é uma função geradora usando `Object.prototype.toString()` e `Function.prototype.call()`.
- Se o resultado da verificação for `'[object GeneratorFunction]'`, então o valor é uma função geradora.

Aqui está o código para a função `isGeneratorFunction`:

```js
const isGeneratorFunction = (val) =>
  Object.prototype.toString.call(val) === "[object GeneratorFunction]";
```

E aqui estão alguns exemplos de como usá-la:

```js
isGeneratorFunction(function () {}); // false
isGeneratorFunction(function* () {}); // true
```
