# Obtendo o Nome do Dia a partir de um Objeto de Data

Para obter o nome do dia da semana a partir de um objeto `Date`, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Date.prototype.toLocaleDateString()` com a opção `{ weekday: 'long' }` para obter o dia da semana.
3.  Você pode usar o segundo argumento opcional para obter um nome específico para um idioma ou omiti-lo para usar a localidade padrão.

Aqui está um exemplo de implementação:

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

Você pode usar esta função assim:

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
