# Como obter a hora com dois pontos de um objeto de data

Se você está procurando praticar a codificação, pode começar abrindo o Terminal/SSH e digitando `node`.

Esta função retorna uma string no formato `HH:MM:SS` a partir de um objeto `Date` fornecido.

Para conseguir isso, os métodos `Date.prototype.toTimeString()` e `String.prototype.slice()` são utilizados para extrair a parte `HH:MM:SS` do objeto `Date`.

Aqui está o código da função:

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

E aqui está um exemplo de uso:

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
