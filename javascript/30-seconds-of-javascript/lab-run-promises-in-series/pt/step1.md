# Executando Promises em Série

Para executar um array de promises em série, use `Array.prototype.reduce()` para criar uma cadeia de promises. Cada promise retorna a próxima promise após ser resolvida.

Para começar, abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

Aqui está um exemplo do código:

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

Você pode então usar a função `runPromisesInSeries` para executar promises sequencialmente, como mostrado no exemplo a seguir:

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// Este código executa cada promise sequencialmente, levando um total de 3 segundos para ser concluído.
```
