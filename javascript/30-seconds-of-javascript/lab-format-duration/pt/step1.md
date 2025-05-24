# Formatar Duração

Para obter o formato legível por humanos de um determinado número de milissegundos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Divida `ms` com os valores apropriados para obter os valores apropriados para `dia`, `hora`, `minuto`, `segundo` e `milissegundo`.
3.  Use `Object.entries()` com `Array.prototype.filter()` para manter apenas os valores não-nulos.
4.  Crie a string para cada valor, pluralizando apropriadamente, usando `Array.prototype.map()`.
5.  Combine os valores em uma string usando `Array.prototype.join()`.

Aqui está o código:

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Aqui estão alguns exemplos:

```js
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574);
// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```
