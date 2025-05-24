# Gerador de Intervalo de Datas

Para gerar todas as datas em um determinado intervalo usando um passo definido, use o seguinte código no Terminal/SSH e digite `node`:

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

Isso cria um gerador que usa um loop `while` para iterar de `start` a `end`, usando o construtor `Date` para retornar cada data no intervalo e incrementa por `step` dias usando `Date.prototype.getDate()` e `Date.prototype.setDate()`.

Para usar um valor padrão de `1` para `step`, omita o terceiro argumento.

Aqui está um exemplo de como usar o `dateRangeGenerator`:

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
