# Verificar se uma Data é um Dia Útil

Para verificar se uma determinada data é um dia útil, você pode usar o seguinte trecho de código:

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- Esta função usa `Date.prototype.getDay()` para obter o dia da semana como um número (0-6), onde Domingo é 0 e Sábado é 6.
- Em seguida, verifica se o dia da semana não é igual a 0 (Domingo) ou 6 (Sábado), o que significa que é um dia útil.
- Se nenhuma data for fornecida como argumento, a data atual é usada como padrão.

Exemplo de uso:

```js
isWeekday(); // true (se a data atual for um dia útil)
isWeekday(new Date(2021, 5, 28)); // true (se a data for um dia útil)
```
