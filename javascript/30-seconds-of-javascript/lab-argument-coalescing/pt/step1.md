# Usando _Argument Coalescing_

Para começar a codificar, abra o Terminal/SSH e digite `node`. _Argument coalescing_ é uma técnica utilizada para retornar o primeiro argumento definido e não nulo em uma lista de argumentos. Para conseguir isso, use `Array.prototype.find()` e `Array.prototype.includes()` para encontrar o primeiro valor que não é igual a `undefined` ou `null`.

Aqui está um exemplo de como usar _argument coalescing_ em JavaScript:

```js
const coalesce = (...args) => args.find((v) => ![undefined, null].includes(v));
```

No trecho de código acima, `coalesce` é uma função que recebe qualquer número de argumentos e retorna o primeiro argumento definido e não nulo. Aqui está um exemplo de como usar a função `coalesce`:

```js
coalesce(null, undefined, "", NaN, "Waldo"); // ''
```

Neste exemplo, `coalesce` é chamada com uma lista de argumentos que inclui `null`, `undefined`, uma string vazia `''`, `NaN` e a string `'Waldo'`. A função retorna uma string vazia `''` porque é o primeiro argumento definido e não nulo na lista.
