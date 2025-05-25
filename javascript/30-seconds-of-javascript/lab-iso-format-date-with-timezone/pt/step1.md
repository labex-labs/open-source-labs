# Convertendo Datas para o Formato ISO com Fuso Horário

Para converter uma data para o formato ISO estendido (ISO 8601), incluindo o deslocamento de fuso horário (timezone offset), siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.
2.  Use `Date.prototype.getTimezoneOffset()` para obter o deslocamento de fuso horário e invertê-lo. Armazene seu sinal em `diff`.
3.  Defina uma função auxiliar, `pad()`, que normaliza qualquer número passado para um inteiro usando `Math.floor()` e `Math.abs()` e o preenche com `2` dígitos, usando `String.prototype.padStart()`.
4.  Use `pad()` e os métodos embutidos no protótipo `Date` para construir a string ISO 8601 com o deslocamento de fuso horário.

Aqui está o código que você pode usar:

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Use a função `toISOStringWithTimezone()` com um objeto `new Date()` como argumento para obter a data no formato ISO com o deslocamento de fuso horário. Por exemplo:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
