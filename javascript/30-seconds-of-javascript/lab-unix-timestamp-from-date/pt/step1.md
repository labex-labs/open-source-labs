# Como Obter o Timestamp Unix a partir de uma Data em JavaScript

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Você pode usar os seguintes passos para obter o timestamp Unix a partir de um objeto `Date` em JavaScript:

1.  Use `Date.prototype.getTime()` para obter o timestamp em milissegundos.
2.  Divida o timestamp por `1000` para obter o timestamp em segundos.
3.  Use `Math.floor()` para arredondar o timestamp resultante para um inteiro.
4.  Se você omitir o argumento `date`, a data atual será usada.

Aqui está um exemplo de trecho de código:

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

Você pode chamar a função `getTimestamp()` para obter o timestamp Unix. Por exemplo:

```js
getTimestamp(); // 1602162242
```
